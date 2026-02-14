import sys
import csv
from _settings import *
from enum import IntEnum

class MapFmt(IntEnum):
    Start = 0
    End = 1
    Type = 2
    Rank = 3
    Symbol = 4
    Next = 5

def _rows():
    with open(getMapFile(), newline='') as f:
        rows = list(csv.reader(f, delimiter=',', quotechar='"'))
        rowslen = len(rows)
        for rowi, row in enumerate(rows):
            if row and row[MapFmt.Start].startswith("0x"):
                #print (row)
                start = int(row[MapFmt.Start], 0)
                end = int(row[MapFmt.End], 0) if row[MapFmt.End] else 0
                next = int(rows[rowi+1][MapFmt.Start], 0) if rowi < rowslen-1 else end
                yield start, end, row[MapFmt.Type], row[MapFmt.Rank], row[MapFmt.Symbol], next

def read_sym_file():
    return list(_rows())

def get_symbol(symbol):
    return next((r for r in _rows() if r[MapFmt.Symbol] == symbol), None)

def get_symbol_with_addrs(start, end):
    return next((r for r in _rows() if r[MapFmt.Start] == start and r[MapFmt.End] == end), None)

