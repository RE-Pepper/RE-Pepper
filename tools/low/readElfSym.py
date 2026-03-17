#!/usr/bin/env python3
from enum import IntEnum
from pathlib import Path
from tools.low.glob import *
from tools.pypstem.callProcess import do_export

class ElfSymFmt(IntEnum):
    Index = 0
    Symbol = 1
    Address = 2
    Scope = 3
    Section = 4
    Type = 5
    Vis = 6
    Size = 7

def read_elfsym(objfile):
    fromelf_flags = ["--only", ".symtab", "-sw", str(objfile)]

    objfile = Path(objfile)
    found = False
    for line in do_export(fromelf_flags, False, True).strip().splitlines():
        row = line.split()

        if "Symbol Name" in line:
            found = True
            continue
        if not found:
            continue

        if len(row) != 8:
            continue

        idx = row[0]
        sym = row[1]
        addr = row[2]
        scope = row[3]
        sect = row[4]
        type = row[5]
        vis = row[6]
        size = row[7]

        if "Ref" == sect or type == "--":
            continue
        if sym in ("[Anonymous", "$a", "$v0", ".emb_text"):
            continue
        if "__ARM" in sym or "BuildAttributes" in sym or "Lib$$Request" in sym or sym.startswith("$d") or sym.startswith("i."):
            continue
        if objfile.stem in sym:
            continue

        yield (idx, sym, addr, scope, sect, type, vis, size)
