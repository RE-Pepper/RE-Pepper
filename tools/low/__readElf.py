#!/usr/bin/env python3
import re
import os
import sys
import subprocess
from io import StringIO
from enum import IntEnum

from tools.low.glob import *

#  __ctr_start                              0x00100000   ARM Code      36  crt0.o(.emb_text)
class ElfMapFmt(IntEnum):
    Symbol = 0
    Address = 1
    Type = 2
    Size = 3
    Section = 4

def _read_elf_symbols():
    if not getOutMapFile().exists():
        fail_ex ("Build Map file not found, readElf cannot be used.", f"Missing: {getMapFile()}")

    with open(getOutMapFile(), "r") as f:
        if not f:
            fail ("Build Map file is empty. Did you finish building?")

        #0x .o
        flag_found = False
        for line in f:
            if not flag_found:
                if "Global Symbols" in line:
                    flag_found = True # got start

                continue

            if not "0x00" in line: # not a sym
                if line.startswith("==="):
                    break # end reached
                continue

            line = [part for part in line.split() if part != "ABSOLUTE"]
            line_len = len(line)
            fmt_len = len(ElfMapFmt)
            #echo (line)
            #echo (line_len)
            #echo (fmt_len)

            sym = line[0]
            addr = int(line[1], 0)
            type = line[2]
            
            if line_len != fmt_len:
                if (line_len-1) != fmt_len:
                    fail_ex ("Unhandled line format in map", line)

                type += f" {line[3]}"
                size = int(line[4])
                sect = line[5]
            else:
                size = int(line[3])
                sect = line[4]

            yield [sym, addr, type, size, sect]

        if not flag_found:
            fail_ex ("Symbols not found in map.", "Ensure you are passing --symbols to linker.")
        

_elf_map_data = {}
for sym in _read_elf_symbols():
    _elf_map_data[sym[ElfMapFmt.Symbol]] = sym

def get_elf_symbol_list():
    return _elf_map_data.values()

def get_elf_symbol(name):
    return _elf_map_data.get(name)
