#!/usr/bin/env python3
# 3differ command line: diff a map symbol between the original binary
# and the built axf. branch targets and pool addresses are normalized,
# so shifted addresses do not poison the score.
#
# usage: python3 tools/3differ/diff.py <version> <symbol|0xADDRESS> [--thumb]

import sys
import argparse
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from tools.low.glob import *
from tools.low.utilsPrint import *
from tools.low.readSymMap import get_symbol, read_sym_file, MapFmt

def main():
    parser = argparse.ArgumentParser(description="3ds function differ")
    parser.add_argument("version", help="Version to diff")
    parser.add_argument("symbol", help="Map symbol name or 0xADDRESS")
    parser.add_argument("--thumb", action="store_true", help="Force thumb decoding")
    parser.add_argument("--full", action="store_true", help="Print the whole function, not only the diff")
    parser.add_argument("--color", action="store_true", help="Force colors")
    args = parser.parse_args()

    setVersion(args.version)

    sym = None
    if args.symbol.startswith("0x"):
        addr = int(args.symbol, 0)
        for r in read_sym_file():
            if r[MapFmt.Start] == addr:
                sym = r
                break
    else:
        sym = get_symbol(args.symbol)

    if sym is None:
        fail_ex ("Symbol not found in map.", args.symbol, False)

    import importlib
    differ = importlib.import_module("tools.3differ")
    res = differ.diff_symbol(sym, thumb_hint=True if args.thumb else None,
                             color=True if args.color else None, full=args.full)
    print (res.stdout)
    sys.exit(res.returncode)

if __name__ == "__main__":
    main()
