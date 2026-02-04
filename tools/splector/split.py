import csv
import os
import shutil
import struct
from bisect import bisect_right
from capstone import *
from capstone.arm import *
from concurrent.futures import ThreadPoolExecutor, as_completed
import re
from _settings import *
from splector._utils import *

BASE_ADDR = 0x00100000
data_start = 0
data_addrs = set() # defined data
addr_done = set() # defined data in functions
datablob_refs = set() # references inside current function
func_refs = set() # all referenced func
switchcases = set() # jumptables inside current function
data_view = [] # all data bytes of program
sym_map = {} # table with symbols (addr: name)

class FakeDataInsn:
    __slots__ = ("address", "size", "id", "mnemonic", "op_str", "operands", "bytes")

    def __init__(self, addr, value=0):
        self.address = addr
        self.size = 4
        self.id = 0
        self.mnemonic = ".word"
        self.op_str = ""
        self.operands = []
        self.bytes = value.to_bytes(4, "little")

    def __repr__(self):
        attrs = ", ".join(f"{k}={getattr(self, k)!r}" for k in self.__slots__)
        return f"<FakeDataInsn {attrs}>"

def get_function(addr, ranges, starts):
    idx = bisect_right(starts, addr) - 1
    if idx >= 0 and ranges[idx][0] <= addr < ranges[idx][1]:
        return ranges[idx]
    return None

import struct

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
    is_func = caller[3] == "f"
    if pc < 0 or pc >= len(data_view):
        return f"@ERROR AT {addr} (ref)"

    val = struct.unpack_from("<I", data_view, pc)[0]
    if is_func and (caller[0] < val < caller[1]): # in callee function
        return f"{'    .word loc_%08X' % val:<84}@ 0x{addr:08X} (local ref)\n"
    elif val in sym_map: # defined symbol
        name = sym_map.get(val)
        return f"{f'    .word {name}':<84}@ 0x{addr:08X} (func ref)\n"
    elif is_func and caller[1] <= val < caller[4]: # part of data blob
        return f"{'    .word 0x%08X' % val:<84}@ 0x{addr:08X} (blob ref)\n"
    else: # treat as any other data
        return f"{'    .word dat_%08X' % val:<84}@ 0x{addr:08X} (data ref)\n"

def dump_data(f):
    start = f[0]
    size = f[1] - f[0]
    for j in range(size): # avoid writing out again
        if (start+j) in addr_done:
            return []
    lines = dump_data_single(f[0], f[1]-f[0], f)
    return lines

def disassemble_func(f):
    pc = f[0] - BASE_ADDR
    size = f[1] - f[0]
    lines = []
    externs = set()
    locals = set()

    md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
    md.detail = True
    md.skipdata = True

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
                fake_instrs.append(FakeDataInsn(addr, struct.unpack_from("<I", data_view, addr - BASE_ADDR)[0]))
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
                if op.type == CS_OP_MEM and op.mem.base == ARM_REG_PC:
                    addr = i.address + 8 + op.mem.disp
                    datablob_refs.add(addr)
                    #if f[0] == 0x1385E0: print(f"{i.address:08X}: {addr:08X}")

                elif op.type == CS_OP_REG and op.reg == ARM_REG_PC:
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
                    datablob_refs.add(addr)
                    #if f[0] == 0x1387C8: print(f"{i.address:08X}: {addr:08X}")

    # Pass 2: Jumptables
    for i_idx, i in enumerate(instrs):
        if i.mnemonic.lower() == "ldrlo": # found jump table / switch case
            datablob_refs.discard(i.address)
            next_idx = i_idx+1
            attempts = 4
            while next_idx < len(instrs):
                nexti = instrs[next_idx]
                attempts -= 1
                val = struct.unpack_from("<I", data_view, nexti.address - BASE_ADDR)[0]
                if not (f[0] <= val < f[1]): # val is not a case
                    if attempts <= 0:
                        break
                    else:
                        continue
                locals.add(val)
                data_addrs.add(nexti.address)
                datablob_refs.discard(nexti.address)
                switchcases.add(nexti.address) # val is a case
                next_idx += 1
            break

        if (i.address in datablob_refs) and (i.address not in switchcases):
            datablob_refs.discard(i.address) # if instr is found data (in function)
            #if f[0] == 0x1387C8: print(f"{i.address:08X}")
            data_addrs.add(i.address)

    # Pass 3: Big Data Scan
    for i_idx, i in enumerate(instrs):
        if (i.address in data_addrs) and (i_idx != 0):
            prev = instrs[i_idx-1]
            if prev.mnemonic.lower() not in ("b", "bx", "pop", "bl"):
                continue
            try_addr = i.address
            while try_addr < (f[4]-4):
                try_addr += 4
                #if f[0] == 0x1387C8: print(f"s{try_addr:08X}")
                if try_addr in locals:
                    break
                #if f[0] == 0x1387C8: print(f"e{try_addr:08X}")
                if try_addr not in data_addrs:
                    #if f[0] == 0x1387C8: print(f"x{try_addr:08X}")
                    data_addrs.add(try_addr)
        
    data_addrs_sort = sorted(data_addrs)
    # Pass 4: Writing the lines
    for i_idx, i in enumerate(instrs):
        if i.address in switchcases:
            continue
        if i.address in addr_done:
                    continue
        if i.address in data_addrs: # check if current instr is actually data        
            """if i_idx == len(instrs) - 1:
                mydatasize = f[1] - i.address # next func start - this addr
                #if mydatasize > 8: print(f"0x{i.address:08X}: size: {mydatasize}, funcend:{f[1]:08X}")
            else:
                addrs_idx = data_addrs_sort.index(i.address)
                mydatasize = min(data_addrs_sort[addrs_idx+1] - i.address, f[1] - i.address) # next addr - this addr
                #if mydatasize > 8: print(f"0x{i.address:08X}: size: {mydatasize}, ref:{data_addrs_sort[addrs_idx+1]:08X}")

            if mydatasize > 40: # experimental
                continue"""
            #if f[0] == 0x1387C8: print(f"ff{i.address:08X}")
            mydatasize = 4
            for line in dump_data_single(i.address, mydatasize, f):
                lines.append(line) # dump em

            for x in range(mydatasize): # notify data not to write again
                addr_done.add(i.address)
            continue

        for ai in range(4):
            addr_done.add(i.address + ai)

        op_str = i.op_str
        op_len = len(i.operands)
        for op_idx, op in enumerate(i.operands):
            if op.type == CS_OP_IMM:
                target = op.imm
                is_local = f[0] <= target < f[1]
                name = f"loc_{target:08X}" if is_local else sym_map.get(target)
                if name is None:
                    continue
                if not is_local:
                    externs.add(name)
                op_str = re.sub(r'#?0x[0-9a-fA-F]+', name, op_str)

        label = ''
        if i.address == f[0]:
            label += f"\n.global {f[2]}\n{f[2]}:\n"
        elif i.address in locals:
            label += f"loc_{i.address:08X}:\n"

        bytes_hex = ''.join(f'{b:02X}' for b in i.bytes)
        lines.append(label + f"    {i.mnemonic:<8} {op_str:<70} @ 0x{i.address:08X} - {bytes_hex}\n")

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
        refss = sorted(datablob_refs)
        for idx, d in enumerate(refss):
            if d in addr_done:
                continue  # already written
            if idx == len(refss) - 1:
                size = f[4] - d
                #if size > 8: print(f"0x{d:08X}: size: {size}, funcend:{f[1]:08X}")
            else:
                size = refss[idx+1] - d
                #if size > 8: print(f"0x{d:08X}: size: {size}, ref:{refss[idx+1]:08X}")
            for line in dump_data_single(d, size, f):
                lines.append(line)
        datablob_refs.clear()
        switchcases.clear()
    return name, externs, lines

def run():
    global data_view, data_start, sym_map
    sym_map, ranges = load_map()

    print("Reading binary...")
    with open(getExeFile(), 'rb') as f:
        data = f.read()
    data_view = memoryview(data)

    md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
    md.detail = True

    clean_dir(getSplitOrigAsmPath())

    print("Preprocessing...")
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

    print("Writing assembly...")

    ranges.sort(key=lambda x: x[0]) # sort it once more
    with open(getSplitOrigAsmPath(), 'w') as out:
        out.write(".section .text\n")
        out.write(".syntax unified\n")

        for f in ranges:
            name, externs, lines = disassemble_symbol(f)

            if len(externs) > 0:
                out.write("\n")
            for e in externs:
                out.write(f".extern {e}\n")
            if len(lines) <= 0:
                continue

            out.writelines(lines)

    count = len(ranges)
    print(f"Wrote {count} symbols to {getSplitOrigAsmPath()}")

if __name__ == "__main__":
    run()

