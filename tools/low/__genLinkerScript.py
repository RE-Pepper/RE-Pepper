#!/usr/bin/env python3
import os
from _settings import *
from low.__parseMap import *
from low.__utilsElf import typeToSectionLinker

def readConfig():
    if not os.path.isfile(getConfFile()):
        return [0,0]
    
    with open(getConfFile(), 'r') as f:
        lines = f.readlines()

    if len(lines) < 4:
        return [0,0]

    roi=int(lines[1].strip(), 0)
    rwi=int(lines[3].strip(), 0)
    ros=str(lines[1].strip())
    rws=str(lines[3].strip())

    return [roi,rwi,ros,rws]

def genLDScript():
    s_code = ''
    s_dataro = ''
    s_datarw = ''

    ro_i, rw_i, ro_s, rw_s = readConfig()
    if ro_i==0 or rw_i==0:
        print(f"Error getting configuration for {get_ver()}!")
        exit(1)

    syms = sorted(read_sym_file(), key=lambda tup: tup[MapFmt.Start])
    for sym_i, sym in enumerate(syms):
        addr = sym[MapFmt.Start]
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
        part += "\t" + name + " 0x{:08x}\n".format(addr)
        part += "\t{\n"
        part += "\t\t* (" + sect + ")\n"
        part += "\t}\n"

        if addr < ro_i:
            s_code += part
        elif addr < rw_i:
            s_dataro += part
        else:
            s_datarw += part

    with open(Path(getProjDir()) / "data" / "template" / "linker.ld", 'r') as template:
        with open(Path(getBuildPath()) / "linker.ld", 'w') as out:

            out_line = template.read().replace("$$$", s_code).replace("&&&", s_dataro).replace("###", s_datarw)
            
            out_line = out_line.replace("§O", ro_s).replace("§W", rw_s)

            out.write(out_line)

def main():
    genLDScript()

if __name__ == '__main__':
    main()
