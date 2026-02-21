#!/usr/bin/env python3
import csv
from _settings import *
from enum import IntEnum

class MapFmt(IntEnum):
    Start = 0
    Pool = 1
    End = 2
    Section = 3
    Rank = 4
    Type = 5
    Symbol = 6

def _rows():
    with open(getMapFile(), newline='') as f:
        rows = list(csv.reader(f, delimiter=',', quotechar='"'))
        rowslen = len(rows)
        for rowi, row in enumerate(rows):
            if len(row) != len(MapFmt):
                continue
            if not (row and row[MapFmt.Start].startswith("0x")):
                continue

            #print (row)
            start = int(row[MapFmt.Start].strip(), 0)
            end = int(row[MapFmt.End].strip(), 0) if row[MapFmt.End].strip() else None
            pool = int(row[MapFmt.Pool].strip(), 0) if row[MapFmt.Pool].strip() else (end if end else 0)
            section = int(row[MapFmt.Section].strip(), 0) if row[MapFmt.Section].strip() else None
            yield start, pool, end, section, row[MapFmt.Rank], row[MapFmt.Type], row[MapFmt.Symbol]

def read_sym_file():
    return list(_rows())

def get_symbol(symbol):
    return next((r for r in _rows() if r[MapFmt.Symbol] == symbol), None)

def get_next(symbol):
    rows = read_sym_file()
    return next((rows[i+1][MapFmt.Start] if i < len(rows)-1 else r[MapFmt.End] for i, r in enumerate(rows) if r[MapFmt.Symbol] == symbol), None)

