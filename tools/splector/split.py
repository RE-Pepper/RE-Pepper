import csv
import os
import shutil
from bisect import bisect_right
from capstone import *
from concurrent.futures import ThreadPoolExecutor, as_completed
import re
from _settings import *
from splector._utils import *

BASE_ADDR = 0x00100000
banned_instr = {"lslsne", "andseq","strbgt", "strbne"}

def get_function(addr, ranges, starts):
    idx = bisect_right(starts, addr) - 1
    if idx >= 0 and ranges[idx][0] <= addr < ranges[idx][1]:
        return ranges[idx]
    return None

def disassemble_function(f, data_view, sym_map, base_addr):
    pc = f[0] - base_addr
    max_len = f[1] - f[0]
    lines = []
    externs = set() # External calls
    locals = set() # Local labels

    md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
    md.detail = True
    instrs = list(md.disasm(data_view[pc:pc+max_len], f[0]))

    if instrs:
        # Pass 1: Local labels
        for i in instrs:
            if i.mnemonic.lower()[0] == 'b':
                for op in i.operands:
                    if op.type == CS_OP_IMM and f[0] <= op.imm < f[1]:
                        locals.add(op.imm)
        # Pass 2: Branches
        for i in instrs:
            op_str = i.op_str
            if i.mnemonic.lower() in banned_instr:
                bytes = f"0x{int.from_bytes(i.bytes, 'little'):08X}"
                lines.append(label + f"    .inst {bytes:<40}  @ 0x{i.address:08X} - {i.mnemonic} {op_str}\n")
                continue

            # Step 1: Resolve name of a branch
            for op in i.operands:
                if op.type != CS_OP_IMM:
                    continue

                target = op.imm
                if f[0] <= target < f[1]:
                    name = f"loc_{target:08X}"
                    locals.add(target) # inside of curr function
                else:
                    name = sym_map.get(target) # try find addr in map
                    if name == None:
                        continue # neither, dont touch

                    externs.add(name) # known symbol

                # replace num with label
                op_str = re.sub(r'#?0x[0-9a-fA-F]+', name, op_str)

            # Step 2: Create label
            label = ''
            if i.address == f[0]:
                label += f"\n.global {f[2]}\n{f[2]}:\n"
            elif i.address in locals:
                label += f"loc_{i.address:08X}:\n"

            # Step 3: Write line
            bytes = ''.join(f'{b:02X}' for b in i.bytes)  # get instruction bytes as hex
            lines.append(label + f"    {i.mnemonic:<8} {op_str:<30} @ 0x{i.address:08X} - {bytes}\n")
    else:
        # raw data
        for offset in range(max_len): # todo: global data handler
            addr = f[0] + offset
            val = data_view[pc + offset]
            lines.append(f"    .byte 0x{val:02X} @ 0x{addr:08X} (data)\n")

    return f[2], sorted(externs), lines

def run():
    sym_map, ranges = load_map()

    print("Reading binary...")
    with open(getExeFile(), 'rb') as f:
        data = f.read()
    data_view = memoryview(data)

    md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
    md.detail = True

    clean_dir(getSplitOrigAsmPath())

    print("Writing assembly...")

    with open(getSplitOrigAsmPath(), 'w') as out:
        out.write(".section .text\n\n")

        with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
            futures = [
                executor.submit(disassemble_function, f, data_view, sym_map, BASE_ADDR)
                for f in ranges
            ]

            for fut in as_completed(futures):
                name, externs, lines = fut.result()

                # externs must appear before use
                for e in externs:
                    out.write(f".extern {e}\n")

                out.write("\n")
                out.writelines(lines)
                out.write("\n")

    count = len(ranges)
    print (f"Wrote {count} symbols to {getSplitOrigAsmPath()}")

if __name__ == "__main__":
    run()

