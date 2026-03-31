#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from tools.low.glob import *
from tools.low.readElfMap import *
from tools.low.readSymMap import *
from tools.low.callAsmdiff import *

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

    res, _ = callAsmdiff(symbol, decomp_symbol, extra_flags, True)
    echo (res)
    if res is None:
        fail (f"End address is invalid for {symbolname}")

if __name__ == "__main__":
    main()
