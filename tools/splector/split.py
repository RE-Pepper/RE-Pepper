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
make it store extensions, and find strings for sjis to store.
"""

md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
md.detail = True
md.skipdata = True

BASE_ADDR = 0x00100000
data_start = 0
data_addrs = set() # defined data
addr_done = set() # defined data in functions
datablob_refs = set() # references inside current function
datablob_ext = set() # part of referenced data inside current function
func_refs = set() # all referenced func
switchcases = set() # jumptables inside current function
switchtable = set() # jumptables inside current function
data_view = [] # all data bytes of program
sym_map = {} # table with symbols (addr: name)

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

    if addr > data_start:
        name = sym_map.get(addr) if addr in sym_map else f"dat_{addr:08X}"
        lines.append(f"\n.global {name}\n{name}:\n")

    while offset < size:
        a = addr + offset
        remaining = size - offset

        if remaining >= 4:
            val = struct.unpack_from("<I", data_view, pc + offset)[0]
            if BASE_ADDR < val < (len(data_view)+BASE_ADDR):
                lines.append(dump_data_ref(a, caller))
            elif val in datablob_ext:
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
    is_func = caller[3] == "f"
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
    size = f[1] - f[0]
    lines = []
    externs = set()
    locals = set()
    datablob_list = {}

    try:
        instrs = list(md.disasm(data_view[pc:pc+size], f[0]))
    except Exception:
        return [], [], []  # fallback handled by caller

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
        if i.operands:
            for op_idx, op in enumerate(i.operands):
                if op.type == CS_OP_MEM and op.mem.base == ARM_REG_PC: # ex: add r1, pc, #0x8
                    addr = i.address + 8 + op.mem.disp
                    datablob_list[i.address] = addr
                    if addr == 0x00185980: echo (f"I am yello {i.address:08X}")

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
                    if addr == 0x00185980: echo (f"I am yelloo {i.address:08X}")

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

        if instrs[i_idx-1].mnemonic.lower() not in ("b", "bx", "pop", "bl"): # find a possible local branch or function end
            continue
        for try_addr in range(i.address, f[4], 4): # from now to function end
            if try_addr == 0x00185980: echo (f"uu {i.address:08X}")
            if try_addr in locals: # detected branch, was blob inside function
                break
            if try_addr >= f[4]: # function end, was blob after function
                break

            if try_addr == 0x00185980: echo (f"aa {i.address:08X}")
            if not try_addr in datablob_ext:
                datablob_ext.add(try_addr)
                if try_addr == 0x00185980: echo (f"oooooo {i.address:08X}")

    datablob_refs.clear()
    # Pass 4: Remove wrong data references
    for ia, addr in datablob_list.items():
        if addr == 0x00185980: echo (f"s {ia:08X} {addr:08X}")
        if addr is None:
            continue
        if ia in datablob_ext and not addr in datablob_ext:
            continue
        if addr == 0x00185980: echo (f"s {ia:08X} {addr:08X}")
        if f[0] > addr > f[4]:
            error_func(f, instrs, f"Reference at 0x{ia:08X} to 0x{addr:08X} is out of function bounds!")

        datablob_refs.add(addr)
    for a in datablob_ext:
        datablob_refs.add(a)

    data_addrs_sort = sorted(data_addrs)
    has_instr = False
    # Pass 5: Writing the lines
    for i_idx, i in enumerate(instrs):
        if i.address == 0x00185980: echo (f"gggg {i.address:08X}")
        if i.address in addr_done:
            continue
        if i.address == 0x00185980: echo (f"gg {i.address:08X}")
        if (i.address in data_addrs) or (i.address in datablob_refs): # check if current instr is actually data
            mydatasize = 4
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
                name = None
                if is_local:
                    if target in switchcases:
                        name = f"case_{target:08X}"
                    else:
                        name = f"loc_{target:08X}"
                else:
                    name = sym_map.get(target)
                if name is None:
                    continue
                if not is_local:
                    externs.add(name)
                op_str = re.sub(r'#?0x[0-9a-fA-F]+', name, op_str)

        # write directives
        label = ''
        if i.address == f[0]:
            label += f"\n.global {f[2]}\n{f[2]}:\n"
        elif i.address in locals:
            if i.address in switchcases:
                label += f"\ncase_{i.address:08X}:\n"
            else:
                label += f"\nloc_{i.address:08X}:\n"

        # write final instruction line
        bytes_hex = ''.join(f'{b:02X}' for b in i.bytes)
        lines.append(label + f"    {i.mnemonic:<8} {op_str:<70} @ 0x{i.address:08X} - {bytes_hex}\n")

    if has_instr == False:
        error_func (f, instrs, f"No instructions!")

    return f[2], sorted(externs), lines

def disassemble_symbol(f):
    if f[0] in addr_done:
        f[2], [], []  # already written
    typ = f[3]
    if typ != "f":
        lines = dump_data(f)
        return f[2], [], lines

    name, externs, lines = disassemble_func(f)
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
    return name, externs, lines

def run():
    global data_view, data_start, sym_map
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
        if(f[3] != "f"):
            size = f[1] - f[0]
            for i in range(size):
                data_addrs.add(f[0]+i)
        else:
            data_start = f[1]

    endaddr = BASE_ADDR + len(data_view) # try find references
    for off in range(0, len(data_view), 4):
        val = struct.unpack_from("<I", data_view, off)[0]
        if (BASE_ADDR < val < endaddr) and (val not in sym_map):
            if val > data_start:
                name = f"dat_{val:08X}"
                sym_map[val] = name
                ranges.append((val, val+4, name, "d"))

    upd_status("Splecting and writing assembly")

    ranges.sort(key=lambda x: x[0]) # sort it once more
    with open(getSplitOrigAsmPath(), 'w') as out:
        out.write(".section .text\n")
        out.write(".syntax unified\n")

        set_status ("Splecting ")

        for f in ranges:
            set_progress (f"0x{f[0]:08X}")
            print_progress()

            name, externs, lines = disassemble_symbol(f)

            if len(externs) > 0:
                out.write("\n")
            for e in externs:
                out.write(f".extern {e}\n")
            if len(lines) <= 0:
                continue

            out.writelines(lines)

            error_exec()

    count = len(ranges)
    echo (f"Wrote {count} symbols to {getSplitOrigAsmPath()}")

if __name__ == "__main__":
    run()

