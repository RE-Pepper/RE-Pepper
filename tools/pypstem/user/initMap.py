#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from tools.pypstem.manSetup import *
from tools.low.readElfSym import *
from tools.low.readHeader import *
from tools.low.updateMap import *
from tools.low.glob import *

sym_list = []
header = None
name_data_list = set()
name_func_list = set()

def convertNames(type,name):
    global name_func_list, name_data_list

    if type in ("f","d"):
        return type

    if "Code" in type:
        if name:
            while name in name_func_list:
                name += "_0"
        name_func_list.add(name)
        return "f", name
    else:
        if name:
            while name in name_data_list:
                name += "_0"
        name_data_list.add(name)
        return "d", name

def addSym(start, end, type, symbol):
    type, name = convertNames(type, symbol)
    sym_list.append((start,None,end,None,"U",type,name))

def main():
    if len(sys.argv) != 2:
        fail ("Parameter: <ver>", False)

    setup_compiler()

    file = getBinFile(sys.argv[1])
    if not file.exists():
        fail ("Executable is missing!", str(file))

    elf_sym_list = read_elfsym(file)
    elf_sym_list = sorted(elf_sym_list, key=lambda s: s[ElfSymFmt.Address])
    
    for s in elf_sym_list:
        name = s[ElfSymFmt.Symbol]
        start = s[ElfSymFmt.Address]
        end = start + s[ElfSymFmt.Size]
        type= s[ElfSymFmt.Type]

        if not type in ("Code", "Data"):
            continue
        if ("<Data" in name):
            continue
        if ("<Func" in name):
            name = None

        addSym(start, end, type, name)
        # TODO: binary analyzer (maybe splector?(ignore thumb?))

    if not sym_list:
        fail ("Symbol List ended up empty!")

    updateFull(sym_list,getMapFile(sys.argv[1]))

if __name__ == "__main__":
    main()
