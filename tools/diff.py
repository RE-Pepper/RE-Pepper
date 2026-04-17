#!/usr/bin/env python3
import os
import sys
import argparse
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from tools.low.glob import *
from tools.low.readElfMap import *
from tools.low.readSymMap import *
from tools.low.callAsmdiff import *
from tools.check import check_sym
from tools.splector.split import split_function

def main():
    parser = argparse.ArgumentParser(description="Build RE:Pepper")
    parser.add_argument("symbol", help="Symbol to diff")
    parser.add_argument("--no_check", '-c', action='store_true', help="Do not recheck")
    parser.add_argument("extra_flags", nargs=argparse.REMAINDER, default=None)
    args = parser.parse_args()
    sys.argv = [sys.argv[0]] # clear args

    symname = args.symbol
    symbol = get_symbol(symname)

    if symbol is None:
        fail_ex (f"Couldn't find in symbol map: {args.symbol}", "Fix the function, or add it to the map!", False)

    symname = symbol[MapFmt.Symbol]
    decomp_symbol = get_elf_symbol(symname)
    if decomp_symbol is None:
        fail_ex (f"Couldn't find in decomp: {args.symbol}", "Make sure to implement this symbol somewhere!", False)

    # make white
    sys.stdout.write("\033[37m")
    sys.stdout.flush()

    # call
    res, _ = callAsmdiff(symbol, decomp_symbol, args.extra_flags, False)
    if res is None:
        fail (f"Assembly diff returned error for {args.symbol}.")

    if not args.no_check:
        check_sym(symname)

if __name__ == "__main__":
    main()
