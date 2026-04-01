#!/usr/bin/env python3
import subprocess

from tools.low.readSymMap import MapFmt
from tools.low.readElfMap import ElfMapFmt
from tools.low.readHeader import *

addr_base = read_header()[HeadType.Text][HeadVal.Start]

def callAsmdiff(map_symbol, decomp_symbol, extra_flags=[], is_json=False):
    if decomp_symbol[ElfMapFmt.Address] == 0:
        return None, 1
    elif decomp_symbol[ElfMapFmt.Address] < addr_base:
        return None, None
    
    sym_start = int(map_symbol[MapFmt.Start]-addr_base)
    decomp_start = int(decomp_symbol[ElfMapFmt.Address]-addr_base)
    sym_size = int(map_symbol[MapFmt.Pool] - map_symbol[MapFmt.Start])
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
