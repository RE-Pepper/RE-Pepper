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

main_data = None
traversed = None
sym = None

def getTypeInc():
    file_path = findFilePath(cfg.flag_preinclude)
    if not file_path:
        fail ("nn/types.h missing, cannot continue.", Fail)

    data, _ = traverseFile (file_path)
    return data

def findFilePath(relative_path):
    if not relative_path:
        fail ("Cannot find empty string for path.")

    try_path = Path(relative_path)
    if try_path.exists():
        return try_path.resolve() # direct path given

    try_path = getProjDir() / relative_path
    if try_path.exists():
        return try_path.resolve() # relative path given

    for possible_dir in base_code_dirs:
        candidate = possible_dir / relative_path
        #print(f"{relative_path}: {candidate}")
        if candidate.exists():
            return candidate

    fail (f"Cannot find file: {relative_path}", False)

def grabInclude(line):
    line_match = re.search(r'"([^"]*)"|<([^>]*)>', line)
    if not line_match:
        return [line], False

    incl_path = line_match.group(1) or line_match.group(2)
    if not incl_path:
        return [line], False

    if cfg.flag_preinclude and incl_path in cfg.flag_preinclude:
        return None, False

    attempt_armcc = Path(os.environ[get_compiler_env_inc()]) / incl_path
    if attempt_armcc.exists():
        return [line], False # do not resolve arm headers

    include_data, _m = traverseFile (incl_path)
    if not include_data or len(include_data) <= 0:
        return None, False
        
    return include_data, True

def traverseFile(pat):
    global main_data, traversed

    if main_data is None: main_data = []
    if traversed is None: traversed = set()

    content = []
    file_path = findFilePath(pat)
    if not file_path or not file_path.exists():
        return None, main_data

    if file_path in traversed:
        return None, main_data

    traversed.add(file_path)

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

        list_lines = getTypeInc()
        if list_lines:
            for l in list_lines: # to be called after anything is written to main_data.
                content.append(l)
    else:
        content.append(f"// File: {file_path.relative_to(getProjDir())}\n")

    with open(file_path, "r", encoding="shift-jis") as f:
        s = f.read().splitlines()
        for line in s:
            if "#pragma once" in line:
                continue

            if "include" in line and "#" in line:
                include_lines, did_include = grabInclude(line)
                if include_lines:
                    content.extend(include_lines)
                    if did_include:
                        content.append (f"// Included from: {file_path.relative_to(getProjDir())}\n")
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

def gen_ctx(path, symbol=None):
    global sym
    sym = symbol

    ctx_data, main_data = traverseFile(path)
    return "\n".join(ctx_data), "\n".join(main_data)

