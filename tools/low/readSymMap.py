#!/usr/bin/env python3
import csv
from enum import IntEnum

from tools.low.glob import *

class MapFmt(IntEnum):
    Start = 0
    Pool = 1
    End = 2
    Section = 3
    Rank = 4
    Type = 5
    Symbol = 6

_map_data = []
if getMapFile().exists():
    with open(getMapFile(), newline='') as f:
        rows = list(csv.reader(f, delimiter=',', quotechar='"'))
        rowslen = len(rows)
        for rowi, row in enumerate(rows):
            if len(row) != len(MapFmt):
                continue
            if not (row and row[MapFmt.Start].startswith("0x")):
                continue

            #echo (row)
            start = int(row[MapFmt.Start].strip(), 0)
            end = int(row[MapFmt.End].strip(), 0) if row[MapFmt.End].strip() else None
            pool = int(row[MapFmt.Pool].strip(), 0) if row[MapFmt.Pool].strip() else (end if end else 0)
            section = int(row[MapFmt.Section].strip(), 0) if row[MapFmt.Section].strip() else None
            _map_data.append((start, pool, end, section, row[MapFmt.Rank], row[MapFmt.Type], row[MapFmt.Symbol]))

def read_sym_file():
    return _map_data

def get_symbol(symbol):
    return next((r for r in _map_data if r[MapFmt.Symbol] == symbol), None)

def get_next(symbol):
    rows = read_sym_file()
    for i, r in enumerate(_map_data):
        if r[MapFmt.Symbol] == symbol:
            if i < len(_map_data) - 1:
                return _map_data[i + 1][MapFmt.Start]
            return r[MapFmt.End]
    return None
