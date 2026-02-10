import os
from _settings import *
from low.__parseMap import *

def readConfig():
    if not os.path.isfile(getConfFile()):
        return [0,0,0]
    
    with open(getConfFile(), 'r') as f:
        lines = f.readlines()

    if len(lines) < 6:
        return [0,0,0]

    ro=str(lines[1].strip())
    rw=str(lines[3].strip())
    rest=str(lines[5].strip())

    return [ro,rw,rest]

def genLDScript():
    data = '\n'
    syms = sorted(read_sym_file(), key=lambda tup: tup[MapFmt.Start])
    for sym in syms:
        if (sym[MapFmt.Symbol] and (sym[MapFmt.Rank] == 'm' or sym[MapFmt.Rank] == 'O')):
            addr = sym[MapFmt.Start]
            type = sym[MapFmt.Type]
            name = sym[MapFmt.Symbol]
            if type == "f" or type == "d":
                sect = "i."+name
            elif type == "fg" or type == "dg":
                sect = ":gdef:"+name
            elif type == "ft":
                sect = "t."+name
            elif type == "dd":
                sect = ".data_"+name
            elif type == "dc":
                sect = ".constdata_"+name
            elif type == "db":
                sect = ".bss_"+name

            data += name + " 0x{:08x}\n".format(addr)
            data += "{\n"
            data += "\t" + name + " 0x{:08x}\n".format(addr)
            data += "\t{\n"
            data += "\t\t* (" + sect + ")\n"
            data += "\t}\n"
            data += "}\n"

    ro, rw, rest = readConfig()

    with open(Path(getProjDir()) / "data" / "template" / "linker.ld", 'r') as template:
        with open(Path(getBuildPath()) / "linker.ld", 'w') as out:

            out_line = template.read().replace("$$$", data)
            
            if len(ro) > 3:
                out_line.replace("§O", ro).replace("§W", rw).replace("§R", rest)

            out.write(out_line)

def main():
    genLDScript()

if __name__ == '__main__':
    main()
