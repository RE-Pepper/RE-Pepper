#!/usr/bin/env python3
import os
tools.low.glob import *
tools.low.__parseMap import *
tools.low.__utilsMap import *
tools.low.__utilsElf import typeToSectionLinker

def endPart(str):
    return str.split('\n', 1)[1] + "\t}\n"

def genLDScript():
    s_code = ''
    s_dataro = ''
    s_datarw = ''

    header = readHeader()
    ro_i = header[HeadType.Ro][HeadVal.Start]
    rw_i = header[HeadType.Rw][HeadVal.Start]
    ro_s = f"0x{ro_i:08X}"
    rw_s = f"0x{rw_i:08X}"

    if ro_i==0 or rw_i==0:
        print(f"Error getting configuration for {get_ver()}!")
        exit(1)

    syms = sorted(read_sym_file(), key=lambda tup: tup[MapFmt.Start])
    for sym_i, sym in enumerate(syms):
        isCreateSection = True
        addr = sym[MapFmt.Start]
        if (addr % 4) != 0:
            isCreateSection = False
        type = sym[MapFmt.Type]
        name = sym[MapFmt.Symbol]
        if not name:
            if "f" in type:
                name = f"fn_{addr:08X}"
            elif "d" in type:
                name = f"dat_{addr:08X}"
            else:
                print(f"Unsupported sym type: {type} at 0x{addr:08X}")
                exit(1)
                
        sect = typeToSectionLinker(type, name)

        part = ""
        if isCreateSection:
            part += "\t}\n"
            part += "\t" + name + " 0x{:08x}\n".format(addr)
            part += "\t{\n"
        part += "\t\t* (" + sect + ")\n"

        if addr < ro_i:
            s_code += part
        elif addr < rw_i:
            s_dataro += part
        else:
            s_datarw += part

    s_code = endPart(s_code)
    s_dataro = endPart(s_dataro)
    s_datarw = endPart(s_datarw)

    with open(Path(getProjDir()) / "data" / "template" / "linker.ld", 'r') as template:
        with open(Path(getBuildPath()) / "linker.ld", 'w') as out:

            out_line = template.read().replace("$$$", s_code).replace("&&&", s_dataro).replace("###", s_datarw)
            
            out_line = out_line.replace("§O", ro_s).replace("§W", rw_s)

            out.write(out_line)

def main():
    genLDScript()

if __name__ == '__main__':
    main()
