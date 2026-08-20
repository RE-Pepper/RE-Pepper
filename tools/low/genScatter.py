#!/usr/bin/env python3
import os
from tools.low.glob import *
from tools.low.readSymMap import *
from tools.low.getSection import typeToSectionLinker
from tools.low.readHeader import *

def endPart(lst):
    if not lst or len(lst) < 1:
        return ""

    return "".join(lst)

def gen_scatter():
    s_code = []
    s_dataro = []
    s_datarw = []
    s_databs = []

    header = read_header()
    tx_s = f"0x{header[HeadType.Text][HeadVal.Start]:08X}"
    ro_s = f"0x{header[HeadType.Ro][HeadVal.Start]:08X}"
    rw_s = f"0x{header[HeadType.Rw][HeadVal.Start]:08X}"

    sym_prev = None
    syms = sorted(read_sym_file(), key=lambda tup: tup[MapFmt.Start])
    for sym_i, sym in enumerate(syms):
        name = sym[MapFmt.Symbol]
        rank = sym[MapFmt.Rank]
        addr = sym[MapFmt.Start]
        if not rank:
            warn(f"Symbol {name} at 0x{addr:08X} is missing the rank!")
            rank = "U"

        type = sym[MapFmt.Type]
        sect = sym[MapFmt.Section]

        if not name:
            if "f" in type:
                name = f"fn_{addr:08X}"
            elif "d" in type:
                name = f"dat_{addr:08X}"
            else:
                fail(f"Unsupported sym type: {type} at 0x{addr:08X}")

        sect_name = sym[MapFmt.SectionName] or typeToSectionLinker(type, name)

        if sym_i == 0:
            sect_str = f"\t\t* ({sect_name}, +FIRST)\n"
        else:
            sect_str = f"\t\t* ({sect_name})\n"

        if "f" in type:
            s_code.append(sect_str)  # func
        elif "d" in type:
            if "b" in type:
                s_databs.append(sect_str)   # dat b
            elif "c" in type:
                s_dataro.append(sect_str)  # dat ro
            else:
                s_datarw.append(sect_str)  # dat rw
        else:
            fail(f"Unsupported sym type: {type} at 0x{addr:08X}")

        sym_prev = sym

    if len(s_code) < 2:
        fail("No functions matching, no scatter created.")
        getOutScatterFile().touch()
        return

    s_code_str = endPart(s_code)
    s_dataro_str = endPart(s_dataro)
    s_datarw_str = endPart(s_datarw)
    s_databs_str = endPart(s_databs)

    out_line = None
    with open(getDataDir() / "template" / "linker.ld", 'r') as f:
        out_line = f.read().replace("///", s_code_str).replace("&&&", s_dataro_str).replace("###", s_datarw_str).replace("???", s_databs_str)
        out_line = out_line.replace("//T", tx_s).replace("//O", ro_s).replace("//W", rw_s)
    with open(getOutScatterFile(), 'w') as f:
        f.write(out_line)

