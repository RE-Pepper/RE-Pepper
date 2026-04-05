#!/usr/bin/env python3
from capstone import *
from capstone.arm import *

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from tools.low.glob import *
from tools.low.readSymMap import *
from tools.low.readHeader import *

def get_asm (sym_name):
    lines = [".syntax unified",f".global {sym_name}",f"{sym_name}:"]
    sym = get_symbol(sym_name)
    if not sym:
        fail (f"Symbol in elf, but not in map: {sym_name}!")

    # read offsets
    base_addr = read_header()[HeadType.Text][HeadVal.Start]
    addr_start = sym[MapFmt.Start] - base_addr
    addr_end_func = sym[MapFmt.End] - base_addr
    if sym[MapFmt.Pool] and sym[MapFmt.Pool] != sym[MapFmt.End]:
        addr_code_size = (sym[MapFmt.Pool]) - base_addr - addr_start
    else:
        addr_code_size = None

    # read binary
    with open(getBinFile(), 'rb') as f:
        data = f.read()
    data_view = memoryview(data)

    # init capstone
    md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
    md.detail = True
    md.skipdata = False

    instrs = list(md.disasm(data_view[addr_start:addr_end_func], 0))

    for i in instrs:
        if addr_code_size and i.address >= addr_code_size:
            # treat as data
            val = struct.unpack_from(">I", data_view, i.address)[0]  # PPC big-endian
            lines.append(f"    .word\t0x{val:08X}")
        else:
            # treat as instruction
            mnem = i.mnemonic
            op_str = i.op_str
            if mnem.startswith("b") and op_str.startswith("#"):
                op_str = op_str.replace("#", "")
            lines.append(f"    {mnem}\t\t{op_str}")

    for l in lines:
        echo (l)
    return "\n".join(lines)

if __name__=="__main__":
    if len(sys.argv) <= 1:
        fail ("Missing argument: Symbol", False)
    asm = get_asm(sys.argv[1])
    echo (asm)
