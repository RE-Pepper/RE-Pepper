#!/usr/bin/env python3
import os
from tools.low.glob import *
from tools.low.readSymMap import *
from tools.low.getSection import typeToSectionLinker
from tools.low.readHeader import *

def endPart(lst):
    lst.pop(0)
    return "".join(lst) + "\t}\n"

def gen_scatter():
    s_code = []
    s_dataro = []
    s_datarw = []
    s_databs = []

    header = read_header()
    tx_s = f"0x{header[HeadType.Text][HeadVal.Start]:08X}"
    ro_s = '+0'
    rw_s = '+0'

    if not cfg.allow_shifting:
        ro_s = f"{header[HeadType.Ro][HeadVal.Start]:08X}"
        rw_s = f"{header[HeadType.Rw][HeadVal.Start]:08X}"

    sym_prev = None
    syms = sorted(read_sym_file(), key=lambda tup: tup[MapFmt.Start])
    for sym_i, sym in enumerate(syms):
        name = sym[MapFmt.Symbol]
        if not name:
            continue
        rank = sym[MapFmt.Rank]
        if cfg.only_matching and rank != 'O':
            continue
        type = sym[MapFmt.Type]
        if not "f" in type and rank == "U":
            continue
        isCreateSection = True
        addr = sym[MapFmt.Start]
        sect = sym[MapFmt.Section]

        if (addr % 4) != 0:
            isCreateSection = False
        if sect and sym_prev and (sect == sym_prev[MapFmt.Section] or sect == sym_prev[MapFmt.Start]):
            isCreateSection = False

        if not name:
            if "f" in type:
                name = f"fn_{addr:08X}"
            elif "d" in type:
                name = f"dat_{addr:08X}"
            else:
                fail(f"Unsupported sym type: {type} at 0x{addr:08X}")

        sect_str = sym[MapFmt.SectionName] or typeToSectionLinker(type, name)

        part = []
        if isCreateSection:
            addr_str = " +0"
            if not cfg.allow_shifting:
                addr_str = f" 0x{addr:08x}\n"
            part.append("\t}\n")
            part.append(f"\ter_{name}{addr_str}")
            part.append("\t{\n")
        part.append(f"\t\t* ({sect_str})\n")

        if "f" in type:
            s_code.extend(part)  # func
        elif "d" in type:
            if "b" in type:
                s_databs.extend(part)   # dat b
            elif "c" in type:
                s_dataro.extend(part)  # dat ro
            else:
                s_datarw.extend(part)  # dat rw
        else:
            fail(f"Unsupported sym type: {type} at 0x{addr:08X}")

        sym_prev = sym

    if len(s_code) < 2:
        fail ("No functions matching, try with --allow_shifting")
        getOutScatterFile().touch()
        return

    s_code_str = endPart(s_code)
    s_dataro_str = endPart(s_dataro) if s_dataro else ''
    s_datarw_str = endPart(s_datarw) if s_datarw else ''
    s_databs_str = endPart(s_databs) if s_databs else ''

    out_line = None
    with open(getDataDir() / "template" / "linker.ld", 'r') as f:
        out_line = f.read().replace("///", s_code_str).replace("&&&", s_dataro_str).replace("###", s_datarw_str).replace("???", s_databs_str)
        out_line = out_line.replace("//T", tx_s).replace("//O", ro_s).replace("//W", rw_s)
    with open(getOutScatterFile(), 'w') as f:
        f.write(out_line)

