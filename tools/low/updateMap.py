#!/usr/bin/env python3
from tools.low.readSymMap import MapFmt
from tools.low.glob import *

# Update map

def make_line(sym):
    line = []
    for col in MapFmt:
        if not sym[col]:
            line.append("          ")
        elif col in (MapFmt.Start, MapFmt.End, MapFmt.Pool):
            line.append(f"0x{sym[col]:08X}")
        else:
            line.append(str(sym[col]))
    return ','.join(line) + '\n'

def updateFull(newsyms, csv_path=None):
    if not csv_path:
        csv_path = getMapFile()
    # Create backup
    with open(csv_path, 'r') as src, open(csv_path + '_b', 'w') as dst:
        dst.write(src.read())

    # Write file
    with open(csv_path, 'w') as f:
        # Write Header
        f.write(','.join(field.name.ljust(10) if field.name in ('Start','Pool','End','Section') else field.name for field in MapFmt) + '\n')

        # Write Symbols
        for sym in newsyms:
            f.write(make_line(sym))

def updateSingle(sym, csv_path=None):
    if not csv_path:
        csv_path = getMapFile()
    # Build line
    sym[MapFmt.Rank] = nowrank
    newline = make_line(sym)

    # Write changes
    file = open(csv_path, "r").readlines()
    for i, line in enumerate(file):
        if symbol_name == line.split(',')[MapFmt.Symbol]:
            file[i] = newline
            break
    with open(csv_path, "w") as f:
        f.writelines(file)
