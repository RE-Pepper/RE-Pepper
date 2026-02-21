#!/usr/bin/env python3
import subprocess
import os
import sys
from _settings import *
from low.__parseElf import *
from low.__parseMap import *

def fail(msg: str):
    print(msg)
    sys.exit(1)

def main():
    if len(sys.argv) < 2:
        fail("diff.py <symbol> [extra flags]")

    symbolname = sys.argv[1]
    extra_flags = sys.argv[2:]

    symbol = get_symbol(symbolname)
    next_symbol = get_next(symbolname)
    decomp_symbol = get_elf_symbol(symbolname)

    if symbol is None:
        fail(f"Couldn't find in csv: {symbolname}")
    if decomp_symbol is None:
        fail(f"Couldn't find in decomp: {symbolname}")

    sym_start = int(symbol[MapFmt.Start]-0x00100000)
    decomp_start = int(decomp_symbol[ElfFmt.Start]-0x00100000)

    sym_size = int(next_symbol - symbol[MapFmt.Start])
    decomp_size = int(decomp_symbol[ElfFmt.Size])
    if decomp_size <= 0:
        decomp_size = sym_size

    if sym_size <= 0:
        fail(f"End address is invalid for {symbolname}")

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
