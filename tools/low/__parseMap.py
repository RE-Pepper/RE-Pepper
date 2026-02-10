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

def _rows():
    with open(getMapFile(), newline='') as f:
        for row in csv.reader(f, delimiter=',', quotechar='"'):
            if row and row[MapFmt.Start].startswith("0x"):
                #print (row)
                start = int(row[MapFmt.Start], 0)
                end = int(row[MapFmt.End], 0) if row[MapFmt.End] else 0
                yield start, end, row[MapFmt.Type], row[MapFmt.Rank], row[MapFmt.Symbol]

def read_sym_file():
    return list(_rows())

def get_symbol(symbol):
    return next((r for r in _rows() if r[MapFmt.Symbol] == symbol), None)

def get_symbol_with_addrs(start, end):
    return next((r for r in _rows() if r[MapFmt.Start] == start and r[MapFmt.End] == end), None)

