#!/usr/bin/env python3
import os
import sys
import subprocess

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from tools.low.glob import *
from tools.low.readElfMap import *
from tools.low.readSymMap import *
from tools.low.readHeader import *

addr_base = read_header()[HeadType.Text][HeadVal.Start]

def main():
    if len(sys.argv) < 2:
        fail ("diff.py <symbol> [extra flags]")

    symbolname = sys.argv[1]
    extra_flags = sys.argv[2:]

    symbol = get_symbol(symbolname)
    decomp_symbol = get_elf_symbol(symbolname)

    if symbol is None:
        fail_ex (f"Couldn't find in symbol map: {symbolname}", "Fix the function, or add it to the map!", False)
    if decomp_symbol is None:
        fail_ex (f"Couldn't find in decomp: {symbolname}", "Make sure to implement this symbol somewhere!", False)

    sym_start = int(symbol[MapFmt.Start]-addr_base)
    decomp_start = int(decomp_symbol[ElfMapFmt.Address]-addr_base)

    sym_size = int(symbol[MapFmt.Pool] - symbol[MapFmt.Start])
    decomp_size = int(decomp_symbol[ElfMapFmt.Size])
    if decomp_size <= 0:
        decomp_size = sym_size

    if sym_size <= 0:
        fail (f"End address is invalid for {symbolname}")

    cmd = [
        sys.executable,
        str(Path(getProjDir()) / "tools" / "asm-differ" / "diff.py"),
        str(sym_start),
        str(decomp_start),
        str(sym_size),
        str(decomp_size)
    ] + extra_flags
    #print(cmd)
    subprocess.run(cmd)

if __name__ == "__main__":
    main()
