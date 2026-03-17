#!/usr/bin/env python3
import re
import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from tools.pypstem.manSetup import *
from tools.pypstem._utils import *
from tools.low.glob import *

# Generate ctx for a single source

base_code_dirs = set()
for mod_path_name, mod_data in cfg.modules.items():
    base_code_dirs.add(getModInc(mod_path_name, mod_data))
    base_code_dirs.add(getModSrc(mod_path_name, mod_data))

setup_compiler(cfg.compiler)

def getTypeInc(sym=None, main_data=None, traversed=None):
    file_path = findFilePath("nn/types.h")
    if not file_path:
        fail ("nn/types.h missing, cannot continue.")

    data, _ = traverseFile (file_path, sym, main_data, traversed)
    return data

def findFilePath(relative_path):
    if not relative_path:
        fail ("Cannot find empty string for path.")

    if Path(relative_path).exists():
        return relative_path # direct path given

    attempt_armcc = Path(os.environ[get_compiler_env_inc()]) / relative_path
    if attempt_armcc.exists():
        return None # do not resolve arm headers

    for possible_dir in base_code_dirs:
        candidate = possible_dir / relative_path
        #print(f"{relative_path}: {candidate}")
        if candidate.exists():
            return candidate

    fail (f"Cannot find file: {relative_path}")

def traverseFile(pat, sym=None, main_data=None, traversed=None):
    if main_data is None:
        main_data = []

    content = []
    file_path = findFilePath(pat)
    if not file_path or not file_path.exists():
        return None, main_data

    if traversed is None: traversed = set()
    if file_path in traversed:
        return None, main_data

    traversed.add(file_path)

    has_includes = False
    is_ns_al = False
    is_main_data = True if main_data is None or len(main_data) == 0 else False
    if is_main_data:
        content.append('#define NON_MATCHING\n')

        if sym:
            content.append(f'// Context for {sym} in {file_path.relative_to(getProjDir())}\n')
            main_data.append(f'// Context for {sym} in {file_path.relative_to(getProjDir())}\n')
        else:
            content.append(f'// Context from {file_path.relative_to(getProjDir())}\n')
            main_data.append(f'// Context from {file_path.relative_to(getProjDir())}\n')
        
        for l in getTypeInc(sym, main_data, traversed): # to be called after anything is written to main_data.
            content.append(l)
    else:
        content.append(f"// File: {file_path.relative_to(getProjDir())}\n")

    with open(file_path, "r", encoding="shift-jis") as f:
        s = f.read().splitlines()
        for line in s:
            if "#pragma once" in line:
                continue

            if "include" in line and "#" in line:
                incl_path = ""
                match = re.search(r'"([^"]*)"|<([^>]*)>', line)
                if not match:
                    continue

                incl_path = match.group(1) or match.group(2)
                if not incl_path:
                    continue

                included, _m = traverseFile (incl_path, sym, main_data, traversed)
                if not included:
                    continue
                    
                for incl_line in included:
                    content.append(incl_line)
                content.append (f"// Included from: {file_path.relative_to(getProjDir())}\n")
                has_includes = True
                continue

            if is_main_data:
                main_data.append(line)
            else:
                content.append (line)
            #if "namespace " in line:
            #    is_ns_al = True


    if is_ns_al == True:
        if is_main_data:
            main_data.append ("Insert code here ...")
            #main_data.append ("}")
        #else:
            #content.append ("}")

    return content, main_data

def gen_ctx(path, symbol):
    ctx_data, main_data = traverseFile(path, symbol)
    return "\n".join(ctx_data), "\n".join(main_data)

