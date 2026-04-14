#!/usr/bin/env python3
import json
import shutil
from pathlib import Path
from collections import defaultdict
import questionary

from tools.low.glob import *
from tools.low.chooser import choose

try:
    import cxxfilt
    is_filter = True
except ImportError:
    echo ("cxxfilt module not found, not demangling.")
    is_filter = False

_sym_file_data = None
with open(getCfgSymsFile(), "r") as f:
    _sym_file_data = json.load(f)

def read_sym_file():
    return _sym_file_data

def get_sym_file(target_sym):
    matches = defaultdict(set)

    for file, syms in _sym_file_data.items():
        if len(syms) < 3:
            echo (f"Skipping symbols entry: {file}")
            continue
        for sym in syms[2:]:
            if target_sym in sym:
                matches[sym].add(file)
            elif is_filter:
                try:
                    demangled = cxxfilt.demangle(sym)
                    if target_sym in demangled:
                        matches[demangled].add(file)
                except cxxfilt.InvalidName:
                    pass

    match_len = len(matches)
    if match_len <= 0:
        echo ("No matches found for "+target_sym)
        return None, target_sym
    
    choices_dict = {
        (sym, file): (file, sym)
        for sym, files in matches.items()
        for file in files
    }

    picked = choose(choices_dict)
    if not picked:
        return None, target_sym

    retval, retsym = picked
    return Path(getProjDir()) / retval, retsym
