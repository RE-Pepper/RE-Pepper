from low.__parseMap import MapFmt
from _settings import *

def write_line(f, sym):
    line = []
    for col in MapFmt:
        if col in (MapFmt.Start, MapFmt.End):
            line.append(f"0x{sym[col]:08X}")
        else:
            line.append(str(sym[col]))
    f.write(','.join(line) + '\n')

def updateFull(newsyms, csv_path=getMapFile()):
    # Create backup
    with open(csv_path, 'r') as src, open(csv_path + '_b', 'w') as dst:
        dst.write(src.read())

    # Write file
    with open(csv_path, 'w') as f:
        # Write Header
        f.write(','.join(field.name for field in MapFmt) + '\n')

        # Write Symbols
        for sym in newsyms:
            write_line(f, sym)

def updateSingle(sym, csv_path=getMapFile()):
    # Build line
    cols = []
    for col in MapFmt:
        if col in (MapFmt.Start, MapFmt.End):
            cols.append(f"0x{sym[col]:08X}")
        elif col == MapFmt.Rank:
            cols.append(nowrank)
        else:
            cols.append(str(sym[col]))
    newline = ",".join(cols) + "\n"

    # Write changes
    file = open(csv_path, "r").readlines()
    for i, line in enumerate(file):
        if symbol_name == line.split(',')[MapFmt.Symbol]:
            file[i] = newline
            break
    with open(csv_path, "w") as f:
        f.writelines(file)
