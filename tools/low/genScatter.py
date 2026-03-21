#!/usr/bin/env python3
import os
from tools.low.glob import *
from tools.low.readSymMap import *
from tools.low.getSection import typeToSectionLinker
from tools.low.readHeader import *

def endPart(str):
    return str.split('\n', 1)[1] + "\t}\n"

def gen_scatter():
    s_code = ''
    s_dataro = ''
    s_datarw = ''

    ro_s = '+0'
    rw_s = '+0'

    if not cfg.allow_shifting:
        header = read_header()
        ro_i = header[HeadType.Ro][HeadVal.Start]
        rw_i = header[HeadType.Rw][HeadVal.Start]
        ro_s = f"0x{ro_i:08X}"
        rw_s = f"0x{rw_i:08X}"

    sym_prev = None
    syms = sorted(read_sym_file(), key=lambda tup: tup[MapFmt.Start])
    for sym in syms:
        rank = sym[MapFmt.Rank]
        if cfg.only_matching and rank != 'O':
            continue
        elif not cfg.allow_shifting and not rank in ("O" "m"):
            continue
        isCreateSection = True
        addr = sym[MapFmt.Start]
        sect = sym[MapFmt.Section]
        type = sym[MapFmt.Type]
        name = sym[MapFmt.Symbol]

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
                fail (f"Unsupported sym type: {type} at 0x{addr:08X}")

        sect_str = typeToSectionLinker(type, name)

        part = ""
        if isCreateSection:
            addr_str = " +0"
            if not cfg.allow_shifting:
                addr_str = f" 0x{addr:08x}\n"
            part +=  "\t}\n"
            part += f"\ter_{name}{addr_str}"
            part +=  "\t{\n"
        part += f"\t\t* ({sect_str})\n"

        if "f" in type:
            s_code += part # func
        elif "d" in type:
            if "c" in type:
                s_dataro += part # dat ro
            else:
                s_datarw += part # dat rw
        else:
            fail (f"Unsupported sym type: {type} at 0x{addr:08X}")

        sym_prev = sym

    s_code = endPart(s_code)
    if s_dataro:
        s_dataro = endPart(s_dataro)
    if s_datarw:
        s_datarw = endPart(s_datarw)

    with open(Path(getProjDir()) / "data" / "template" / "linker.ld", 'r') as template:
        with open(getOutScatterFile(), 'w') as out:

            out_line = template.read().replace("///", s_code).replace("&&&", s_dataro).replace("###", s_datarw)
            
            out_line = out_line.replace("//O", ro_s).replace("//W", rw_s)

            out.write(out_line)

def main():
    genLDScript()

if __name__ == '__main__':
    main()
