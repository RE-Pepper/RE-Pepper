import csv
import os
import shutil
from bisect import bisect_right
from capstone import *
from concurrent.futures import ThreadPoolExecutor, as_completed
import re
from low.__parseMap import read_sym_file
from _settings import *

BASE_ADDR = 0x00100000

def check_symbol(name, addr):
    if not name or name.strip() == "":
        return f"fn_{addr:08X}"
    return name

def load_map():
    print("Loading map...")
    sym_map = {}
    ranges = []
    read_sym_file
    for sym in read_sym_file():
        if rank == 'O':
            continue
        if name:
            sym_map[sym[0]] = sym[3]
        if sym[2] > 0:
            ranges.append({sym[0], sym[0] + sym[2], sym[3]}) # start, end, name
    ranges.sort(key=lambda x: x[0])
    return sym_map, ranges

def sort_map(ranges):
    return [f[0] for f in ranges]

def get_function(addr, ranges, starts):
    idx = bisect_right(starts, addr) - 1
    if idx >= 0 and ranges[idx][0] <= addr < ranges[idx][1]:
        return ranges[idx]
    return None

def disassemble_function(f, data_view, sym_map, referenced_locals, base_addr):
    pc = f[0] - base_addr
    max_len = f[1] - f[0]
    lines = []
    externs = set()

    md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
    md.detail = True
    instrs = list(md.disasm(data_view[pc:pc+max_len], f[0]))

    if instrs:
        for i in instrs:
            op_str = i.op_str
            for op in i.operands:
                if op.type == CS_OP_IMM:
                    target = op.imm
                    if f[0] <= target < f[1]:
                        name = f"loc_{target:08X}"
                    else:
                        name = sym_map.get(target, f"fn_{target:08X}")
                        externs.add(name)
                    # replace any immediate literal with label
                    op_str = re.sub(r'#?0x[0-9a-fA-F]+', name, op_str)
            # labels
            label = ''
            if i.address == f[0]:
                label += f"\n.global {f[2]}\n{f[2]}:\n"
            elif i.address in referenced_locals:
                label += f"loc_{i.address:08X}:\n"
            lines.append(label + f"    {i.mnemonic:<8} {op_str:<30} @ 0x{i.address:08X}\n")
    else:
        # raw data
        for offset in range(max_len):
            addr = f[0] + offset
            val = data_view[pc + offset]
            lines.append(f"    .byte 0x{val:02X} @ 0x{addr:08X} (data)\n")

    return f[2], sorted(externs), lines

def run():
    sym_map, ranges = load_map()
    starts = sort_map(ranges)

    print("Reading binary...")
    with open(getExeFile(), 'rb') as f:
        data = f.read()
    data_view = memoryview(data)

    md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
    md.detail = True

    print("Pass 1: Finding local jumps...")
    referenced_locals = set()
    pc = 0
    total_size = len(data)
    while pc < total_size:
        curr_addr = BASE_ADDR + pc
        current_func = get_function(curr_addr, ranges, starts)
        if current_func:
            max_len = min(current_func[1] - curr_addr, total_size - pc)
            instrs = list(md.disasm(data_view[pc:pc+max_len], curr_addr))
            if instrs:
                for i in instrs:
                    for op in i.operands:
                        if op.type == CS_OP_IMM and current_func[0] <= op.imm < current_func[1]:
                            referenced_locals.add(op.imm)
                    pc += i.size
            else:
                referenced_locals.add(curr_addr)
                pc += 1
        else:
            next_idx = bisect_right(starts, curr_addr)
            next_addr = ranges[next_idx][0] if next_idx < len(ranges) else total_size + BASE_ADDR
            pc += next_addr - curr_addr

    print("Pass 2: writing assembly...")
    if os.path.exists(getSplitAsmPath()):
        shutil.rmtree(getSplitAsmPath())
    os.makedirs(getSplitAsmPath(), exist_ok=True)

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = [
            executor.submit(disassemble_function, f, data_view, sym_map, referenced_locals, BASE_ADDR)
            for f in ranges
        ]
        for fut in as_completed(futures):
            name, externs, lines = fut.result()
            path = os.path.join(getSplitAsmPath(), f"{name}.s")
            with open(path, 'w') as out_file:
                out_file.write(".section .text\n\n")
                for e in externs:
                    out_file.write(f".extern {e}\n")
                out_file.writelines(lines)

if __name__ == "__main__":
    run()

