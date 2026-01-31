import os
import shutil
from low.__parseMap import read_sym_file

def clean_dir(path):
    out_dir = os.path.dirname(path)
    if os.path.exists(out_dir):
        print("Output exists, deleting...")
        shutil.rmtree(out_dir)
    os.makedirs(out_dir, exist_ok=True)

def check_fname(name, addr):
    if not name or name.strip() == "":
        return f"fn_{addr:08X}"
    return name

def load_map():
    print("Loading map...")
    sym_map = {}
    ranges = []
    read_sym_file
    for sym in read_sym_file():
        name = check_fname(sym[3], sym[0]) # valid name
        
        if sym[0] != 0x00100000: # skip __ctr_start
            sym_map[sym[0]] = name

        if sym[1] == 'O': # Matched
            continue
        if sym[2] <= 0: # Size 0
            continue

        ranges.append((sym[0], sym[0] + sym[2], name)) # start, end, name

    ranges.sort(key=lambda x: x[0])
    return sym_map, ranges
