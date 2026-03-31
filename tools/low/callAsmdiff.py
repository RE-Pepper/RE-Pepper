#!/usr/bin/env python3
import subprocess

from tools.low.readSymMap import MapFmt
from tools.low.readElfMap import ElfMapFmt
from tools.low.readHeader import *

addr_base = read_header()[HeadType.Text][HeadVal.Start]

def callAsmdiff(symbol, decomp_symbol, extra_flags=[], is_json=False):
    sym_start = int(symbol[MapFmt.Start]-addr_base)
    decomp_start = int(decomp_symbol[ElfMapFmt.Address]-addr_base)
    sym_size = int(symbol[MapFmt.Pool] - symbol[MapFmt.Start])
    decomp_size = int(decomp_symbol[ElfMapFmt.Size])

    if decomp_size <= 0:
        decomp_size = sym_size
    if sym_size <= 0:
        return None, None

    cmd = [
        sys.executable,
        str(Path(getProjDir()) / "tools" / "asm-differ" / "diff.py"),
        str(sym_start),
        str(decomp_start),
        str(sym_size),
        str(decomp_size),
        "-I", "-i"
    ]

    if is_json:
        cmd.append("--format json")

    if extra_flags:
        cmd.extend(extra_flags)

    if is_json:
        err = subprocess.run(" ".join(cmd), shell=True, capture_output=True, text=True)
    else:
        err = subprocess.run(cmd)

    return err, sym_size
