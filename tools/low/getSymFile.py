#!/usr/bin/env python3
import json
import shutil
from pathlib import Path
from collections import defaultdict
import questionary

from tools.low.glob import *

try:
    import cxxfilt
    is_filter = True
except ImportError:
    echo ("cxxfilt module not found, not demangling.")
    is_filter = False

maxlen = 0

def _entryString(sym, file):
    return f"{sym:<{maxlen}}    {file}"

def get_sym_file(target_sym):
    global maxlen

    with open(getCfgSymsFile(), "r") as f:
        data = json.load(f)

    matches = defaultdict(set)

    for file, syms in data.items():
        for sym in syms:
            if target_sym in sym:
                matches[sym].add(file)
                if len(sym) > maxlen:
                    maxlen = len(sym)
            elif is_filter:
                try:
                    sym = cxxfilt.demangle(sym)
                    if target_sym in sym:
                        matches[sym].add(file)
                        if len(sym) > maxlen:
                            maxlen = len(sym)
                except cxxfilt.InvalidName:
                    pass

    retfile = None
    retsym = None

    match_len = len(matches)
    if match_len <= 0:
        echo ("No matches found for "+target_sym)
        return None, target_sym
    elif match_len == 1:
        sym, files = next(iter(matches.items()))
        retval = next(iter(files))
        retsym = sym
    else:
        choices = [
            questionary.Choice(title=_entryString(sym, file), value=(file,sym))
            for sym, files in matches.items()
            for file in files
        ]
        retval, retsym = questionary.select(
                message="Multiple matches found! Please select one: ",
                choices=choices).ask()
                
    return Path(getProjDir()) / retval, retsym

