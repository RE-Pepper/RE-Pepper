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
    decomp_symbol = get_elf_symbol(symbolname)

    if symbol is None:
        fail(f"Couldn't find in csv: {symbolname}")
    if decomp_symbol is None:
        fail(f"Couldn't find in decomp: {symbolname}")

    sym_size = int(symbol[MapFmt.End] - symbol[MapFmt.Start])
    decomp_size = int(decomp_symbol[ElfFmt.Size])
    if decomp_size == 0:
        print(f"Warning: decomp symbol size for {symbol[3]} is 0. Using the original size instead.")
        decomp_size = sym_size

    cmd = [
        sys.executable,
        str(Path(getProjDir()) / "tools" / "asm-differ" / "diff.py"),
        str(symbol[MapFmt.Start]-0x00100000),
        str(decomp_symbol[ElfFmt.Start]-0x00100000),
        str(sym_size),
        str(decomp_size)
    ] + extra_flags

    subprocess.run(cmd)

if __name__ == "__main__":
    main()
