import os
import shutil
from low.__parseMap import *
from enum import IntEnum

def clean_dir(path):
    out_dir = os.path.dirname(path)
    if os.path.exists(out_dir):
        print ("Output exists, deleting...")
        shutil.rmtree(out_dir)
    os.makedirs(out_dir, exist_ok=True)

def check_name(name, typ, addr):
    if not name or name.strip() == "":
        if (typ == "f"):
            return f"fn_{addr:08X}"
        elif (typ is None or typ == ""):
            return f"unk_{addr:08X}"
        else:
            return f"dat_{addr:08X}"
    return name

def load_map():
    print ("Loading map...")
    sym_map = {}
    ranges = []
    syms = read_sym_file()
    symlen = len(syms)
    for i in range(symlen):
        sym = syms[i]
        start = sym[MapFmt.Start]
        end = sym[MapFmt.End]
        typ = sym[MapFmt.Type]
        next = syms[i+1][MapFmt.Start] if (i != symlen-1) else end
        name = check_name(sym[MapFmt.Symbol], typ, start) # valid name
        
        if start != 0x00100000: # skip __ctr_start
            sym_map[start] = name

        if (end > next) and (typ == "f"):
            print (f"OVERLAP! {name} touching next symbol.")

        if sym[MapFmt.Rank] == 'O': # Matched
            continue
        if end is None or end <= 0:
            if symlen < i+1:
                print ("Last symbol has no end.")
            elif symlen > (i+1):
                end = syms[i+1][MapFmt.Start]

        ranges.append((start, end, name, typ, next))

    ranges.sort(key=lambda x: x[0])
    return sym_map, ranges
