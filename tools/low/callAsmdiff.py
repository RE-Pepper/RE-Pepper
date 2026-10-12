#!/usr/bin/env python3
import importlib
from typing import Callable, Optional

from tools.low.glob import *
from tools.low.readSymMap import MapFmt
from tools.low.readElfMap import ElfMapFmt

# ranks a map row against the build using 3differ (capstone, no
# devkitpro). returns (DiffResult, size), the result mimics the old
# subprocess protocol: .returncode (0 = tool ok, a diff is not a
# failure), .stdout with CURRENT (N), diff_change/add/remove markers.

def callAsmdiff(map_symbol, decomp_symbol, extra_flags=[], is_json=False):
    if decomp_symbol[ElfMapFmt.Address] == 0:
        return None, None
    elif decomp_symbol[ElfMapFmt.Address] < getHeaderLo():
        return None, None

    sym_size = map_symbol[MapFmt.End] - map_symbol[MapFmt.Start]
    if sym_size <= 0:
        return None, None

    differ = importlib.import_module("tools.3differ")
    res = differ.diff_symbol(map_symbol, color=False)
    return res, sym_size

def getHeaderLo():
    from tools.low.readHeader import read_header, HeadType, HeadVal
    return read_header()[HeadType.Text][HeadVal.Start]
