import sys
import csv
from _settings import *

import csv
from _settings import *

def _rows():
    with open(getFuncSymFile(), newline='') as f:
        for row in csv.reader(f, delimiter=',', quotechar='"'):
            if row and row[0].startswith("0x"):
                addr = int(row[0], 0) if row[0] else 0
                size = int(row[2], 0) if row[2] else 0
                yield addr, row[1], size, row[3], row[4]

def read_sym_file():
    return list(_rows())

def get_symbol(symbol):
    return next((r for r in _rows() if r[3] == symbol), None)

def get_symbol_with_addr_and_size(addr, size):
    return next((r for r in _rows() if r[0] == addr and r[2] == size), None)

