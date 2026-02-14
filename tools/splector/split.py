import csv
import os
import shutil
import struct
from capstone import *
from capstone.arm import *
from concurrent.futures import ThreadPoolExecutor, as_completed
import re
from _settings import *
from splector._utils import *

"""
TODO:
datablob_ext
make it find strings for sjis to store.
"""

md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
md.detail = True
md.skipdata = True

BASE_ADDR = 0x00100000
data_start = 0
data_end = 0
data_addrs = set() # defined data
addr_done = set() # defined data in functions
datablob_refs = set() # references inside current function
datablob_ext = set() # part of referenced data inside current function
func_refs = set() # all referenced func
switchcases = set() # jumptables inside current function
switchtable = set() # jumptables inside current function
data_view = [] # all data bytes of program
sym_map = {} # table with symbols (addr: name)
ranges = [] # symbol map all
ranges_data = [] # symbol map data

class FakeDataInsn:
    __slots__ = ("address", "size", "id", "mnemonic", "op_str", "operands", "bytes")

    def __init__(self, addr, raw_bytes):
        self.address = addr
        self.size = 4
        self.id = 0
        self.mnemonic = ".word"
        self.op_str = ""
        self.operands = []
        self.bytes = bytes(raw_bytes)

    def __repr__(self):
        attrs = ", ".join(f"{k}={getattr(self, k)!r}" for k in self.__slots__)
        return f"<FakeDataInsn {attrs}>"

def dump_data_single(addr, size, caller):
    lines = []
    
    pc = addr - BASE_ADDR
    if pc < 0 or pc >= len(data_view):
        return lines
    size = min(size, len(data_view) - pc)
    offset = 0

    if addr in addr_done:
        return lines
    else:
        for ai in range(size):
            a = addr + ai
            addr_done.add(a)

    while offset < size:
        a = addr + offset
        remaining = size - offset

        if remaining >= 4:
            val = struct.unpack_from("<I", data_view, pc + offset)[0]
            if BASE_ADDR < val < (len(data_view)+BASE_ADDR):
                lines.append(dump_data_ref(a, caller))
            else:
                lines.append(f"{'    .word 0x%08X' % val:<84}@ 0x{a:08X} (data)\n")
            offset += 4

        elif remaining >= 2:
            val = struct.unpack_from("<H", data_view, pc + offset)[0]
            lines.append(f"{'    .hword 0x%04X' % val:<84}@ 0x{a:08X} (data)\n")
            offset += 2

        else:
            val = data_view[pc + offset]
            lines.append(f"{'    .byte 0x%02X' % val:<84}@ 0x{a:08X} (data)\n")
            offset += 1
    return lines

def dump_data_ref(addr, caller): # 
    pc = addr - BASE_ADDR
    is_func = (not caller is None) and caller[3].startswith("f")
    out = f"@ERROR AT {addr} (ref)"
    if pc < 0 or pc >= len(data_view):
        return out

    val = struct.unpack_from("<I", data_view, pc)[0] # get 4 byte word

    str = ["data ref", f"0x{val:08X}"] # type, data

    if is_func: # check is function
        if caller[0] < val < caller[1]: # inside of callee function
            if val in switchcases:
                str = ["switch case", f"case_{val:08X}"]
            else: # just local
                str = ["local ref", f"loc_{val:08X}"]
        elif (val in sym_map) and (caller[1] < val >= caller[4]): # defined symbol
            str = ["func ref" if val < data_start else "data ref", sym_map.get(val)]
    elif (val in sym_map): # treat as any other data ( found in preprocessing )
        str = ["data ref", sym_map.get(val)]

    return f"{f'    .word {str[1]}':<84}@ 0x{addr:08X} ({str[0]})\n"

def dump_data(f):
    start = f[0]
    size = f[1] - f[0]
    for j in range(size): # avoid writing out again
        if (start+j) in addr_done:
            return []
    lines = dump_data_single(f[0], f[1]-f[0], f)
    return lines
    

def disassemble_func(f):
    global md, datablob_refs

    pc = f[0] - BASE_ADDR
    size = f[4] - f[0]
    name = f[2]
    lines = []
    externs = set()
    locals = set()
    datablob_list = {}

    instrs = list(md.disasm(data_view[pc:pc+size], f[0]))

    # Pass 0: Fake instruction generation and local labels
    for i_idx, i in enumerate(instrs):
        if i.id == 0: # is ignored data blob, generate fake instructions for data
            blob_start = i.address
            blob_end = i.address + i.size

            fake_instrs = []
            addr = blob_start
            while addr < blob_end:
                fake_instrs.append(FakeDataInsn(addr, data_view[addr - BASE_ADDR : addr - BASE_ADDR + 4]))
                addr += 4

            instrs[i_idx:i_idx+1] = fake_instrs
            continue

        if i.mnemonic.lower().startswith('b'):
            op = i.operands[0]
            if op.type == CS_OP_IMM and f[0] <= op.imm < f[1]:
                locals.add(op.imm)

    # Pass 1: Find data refs
    for i_idx, i in enumerate(instrs):
        if i.bytes == b'\x00\x00\x00\x00':
            datablob_list[i.address] = i.address
        elif i.operands:
            for op_idx, op in enumerate(i.operands):
                if (op.type == CS_OP_MEM or op.type == ARM_OP_MEM) and op.mem.base == ARM_REG_PC: # ex: add r1, pc, #0x8
                    addr = i.address + 8 + op.mem.disp
                    datablob_list[i.address] = addr

                elif op.type == CS_OP_REG and op.reg == ARM_REG_PC: # ex: ldr r1, [pc, #0x8]
                    if len(i.operands) < 3 or op_idx >= len(i.operands)-1:
                        continue
                    prev = i.operands[op_idx-1]
                    next = i.operands[op_idx+1]
                    if (prev.type != CS_OP_REG) or (prev.reg == ARM_REG_LR):
                        continue
                    if next.type != CS_OP_IMM:
                        continue
                    if i.mnemonic.lower().startswith("sub"):
                        addr = i.address + 8 - next.imm
                    else:
                        addr = i.address + 8 + next.imm
                    datablob_list[i.address] = addr

    # Pass 2: Jumptables
    for i_idx, i in enumerate(instrs):
        if i.mnemonic.lower() == "ldrlo": # found jump table / switch case
            datablob_list[i.address] = None
            next_idx = i_idx+1
            attempts = 4
            while next_idx < len(instrs):
                nexti = instrs[next_idx]
                attempts -= 1
                val = struct.unpack_from("<I", data_view, nexti.address - BASE_ADDR)[0]
                if not (f[0] <= val < f[1]): # val is not a case
                    if attempts <= 0:
                        next_idx = len(instrs)
                    else:
                        next_idx += 1
                    continue
                # if here, we got a case.
                attempts = 0
                locals.add(val)
                data_addrs.add(nexti.address)
                datablob_list[nexti.address] = None
                switchcases.add(val)
                switchtable.add(nexti.address)
                next_idx += 1
            continue

    datablob_set = set(v for v in datablob_list.values() if v is not None)
    # Pass 3: Bigger Data scan
    for i_idx, i in enumerate(instrs):
        if i_idx == 0 or not (i.address in data_addrs or i.address in datablob_set):
            continue
        # this is ref. data
        if i.address in switchtable: # skip jtables
            continue

        # find a possible local branch or function end
        prev = instrs[i_idx-1]
        mnem = prev.mnemonic.lower()
        if not mnem in ("b", "bx", "pop", "bl"):
            continue

        for try_addr in range(i.address, f[4], 4): # from now to function end
            if try_addr in locals: # detected branch, was blob inside function
                break
            if try_addr >= f[4]: # function end, was blob after function
                break

            if not try_addr in datablob_ext:
                datablob_ext.add(try_addr)

    datablob_refs.clear()
    # Pass 4: Remove wrong data references
    for ia, addr in datablob_list.items():
        if addr is None:
            continue
        if ia in datablob_ext and not addr in datablob_ext:
            continue
        if f[5] and (addr < f[0] or addr >= f[4]):
            error_func(f, instrs, f"Reference at 0x{ia:08X} to 0x{addr:08X} is out of function bounds!")

        datablob_refs.add(addr)
    for a in datablob_ext:
        datablob_refs.add(a)

    data_addrs_sort = sorted(data_addrs)
    has_instr = False
    # Pass 5: Writing the lines
    for i_idx, i in enumerate(instrs):
        if i.address in addr_done:
            continue
        # check if current instr is actually data
        if (i.address in data_addrs) or (i.address in datablob_refs) or (i.address > f[1]):
            mydatasize = 4 # find size if possible, else 4
            if i.address in sym_map:
                for sym in ranges_data:
                    if sym != i.address:
                        continue

                    if sym[1] and sym[1] > sym[0]:
                        mydatasize = sym[1] - sym[0]
                    break

            for line in dump_data_single(i.address, mydatasize, f):
                lines.append(line) # dump em

            for x in range(mydatasize): # notify data not to write again
                addr_done.add(i.address)
            continue

        # this is an instruction.
        has_instr = True
        for ai in range(4): # mark every byte as done
            addr_done.add(i.address + ai)

        # replace label refs
        op_str = i.op_str
        op_len = len(i.operands)
        for op_idx, op in enumerate(i.operands):
            if op.type == CS_OP_IMM:
                target = op.imm
                is_local = f[0] <= target < f[1]
                labelname = None
                if is_local:
                    if target in switchcases:
                        labelname = f"case_{target:08X}"
                    else:
                        labelname = f"loc_{target:08X}"
                elif target < data_start:
                    labelname = sym_map.get(target)
                if labelname is None:
                    continue
                if not is_local:
                    externs.add(labelname)
                op_str = re.sub(r'#?0x[0-9a-fA-F]+', labelname, op_str)

        # write directives
        label = ''
        if i.address == f[0]:
            label += f"\n.global {name}"
            label += f"\n.type {name} %function"
            label += f"\n{name}:\n"
        elif i.address in locals:
            if i.address in switchcases:
                label += f"\ncase_{i.address:08X}:\n"
            else:
                label += f"\nloc_{i.address:08X}:\n"

        # write final instruction line
        bytes_hex = ''.join(f'{b:02X}' for b in i.bytes)
        lines.append(label + f"    {i.mnemonic:<8} {op_str:<70} @ 0x{i.address:08X} - {bytes_hex}\n")

    lines.append(f".size {name}, .-{name}\n")

    if has_instr == False:
        error_func (f, instrs, f"No instructions!")

    return sorted(externs), lines

def disassemble_symbol(f):
    if f[0] in addr_done:
        return [], []  # already written

    if not f[3].startswith("f"):
        lines = dump_data(f)
        return [], lines

    externs, lines = disassemble_func(f)
    if not lines: # not a valid function after all
        lines = dump_data(f)
    else: # valid function
        blob = sorted(datablob_refs)
        for idx, d in enumerate(blob):
            if d in addr_done:
                continue  # already written
            if idx == len(blob) - 1:
                size = f[4] - d
            else:
                size = blob[idx+1] - d
            for line in dump_data_single(d, size, f):
                lines.append(line)
        datablob_refs.clear()
        datablob_ext.clear()
        switchcases.clear()
        switchtable.clear()
    return externs, lines

data_lastname = None
def assemble_data(addr):
    global data_lastname

    lines = []
    size = 4

    if addr in addr_done:
        return []

    # get size
    if addr in sym_map:
        if data_lastname:
            lines.append(f".size {data_lastname}, .-{data_lastname}\n")
        data_lastname = sym_map.get(addr)
        lines.append(f"\n.global {data_lastname}")
        lines.append(f"\n.type {data_lastname} %object")
        lines.append(f"\n{data_lastname}:\n")

        next = min((a for a in sym_map if a > addr), default=data_end)
        size = next - addr # get next start address in map

        for sym in ranges_data:
            if addr == sym[0]:
                if sym[3] == "db": # skip bss
                    return []
                if sym[1] and sym[1] > addr:
                    size = sym[1] - addr
                break

    for line in dump_data_single(addr, size, None):
        lines.append(line)

    return lines

def run():
    global data_view, data_start, data_end, sym_map, ranges
    sym_map, ranges = load_map()

    upd_status("Reading binary")
    with open(getExeFile(), 'rb') as f:
        data = f.read()
    data_view = memoryview(data)

    md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
    md.detail = True

    clean_dir(getSplitOrigAsmPath())

    upd_status("Preprocessing")
    for f in ranges: # find all data symbols
        if f[3].startswith("d"):
            size = f[1] - f[0]
            data_addrs.add(f[0])
        else:
            data_start = f[1]

    endaddr = BASE_ADDR + len(data_view) # try find references
    for off in range(0, len(data_view), 4):
        val = struct.unpack_from("<I", data_view, off)[0]
        if (BASE_ADDR < val < endaddr) and (val not in sym_map):
            if val > data_start:
                dataname = f"dat_{val:08X}"
                sym_map[val] = dataname
                ranges.append((val, val+4, dataname, "d"))

    if len(sys.argv) > 1:
        skipToAddr = int(sys.argv[1], 0)
    else:
        skipToAddr = 0

    upd_status("Splecting and writing assembly")

    # Start writing data
    ranges.sort(key=lambda x: x[0]) # sort it once more
    with open(getSplitOrigAsmPath(), 'w') as out:
        out.write(".section .text\n")
        out.write(".syntax unified\n")

        set_status ("Splecting map ")

        # Write out functions
        for f in ranges:
            if f[0] >= data_start:
                continue
            if f[0] < skipToAddr:
                set_progress (f"FF 0x{f[0]:08X}")
                continue
            set_progress (f"0x{f[0]:08X}")
            print_progress()

            externs, lines = disassemble_symbol(f)

            if len(externs) > 0:
                out.write("\n")
            for e in externs:
                out.write(f".extern {e}\n")
            if len(lines) <= 0:
                continue

            out.writelines(lines)

            error_exec()

        set_status ("Splecting data ")

        count = len(ranges)
        # Rewrite ranges
        for sym in ranges:
            if sym[3].startswith("d"):
                ranges_data.append(sym)

        # Write out data
        data_end = len(data_view) + BASE_ADDR
        for addr in range(data_start, data_end, 4):
            if addr < skipToAddr:
                set_progress (f"FF 0x{addr:08X}")
                continue
            set_progress (f"0x{addr:08X}")
            print_progress()

            lines = assemble_data(addr)

            if len(lines) <= 0:
                continue

            out.writelines(lines)
                

    if skipToAddr != 0:
        echo (f"SPLIT INCOMPLETE, STARTED FROM {skipToAddr}")
    echo (f"Wrote {count} symbols to {getSplitOrigAsmPath()}")

if __name__ == "__main__":
    run()

