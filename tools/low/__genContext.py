#!/usr/bin/env python3
import os
import re
from io import StringIO
from pathlib import Path

include_paths = [
    "lib",
    "Game/src",
    "Game/include",
    "lib/al/include",
    "lib/sead/include",
    "lib/NintendoWare/anim/include",
    "lib/NintendoWare/font/include",
    "lib/NintendoWare/gfx/include",
    "lib/NintendoWare/lyt/include",
    "lib/NintendoWare/project/include",
    "lib/NintendoWare/snd/include",
    "lib/NintendoWare/sys/include",
    "lib/NintendoWare/ut/include",
    "lib/CTRSDK/include",
    "lib/sead/addins/libms/include",
]

def getTypeInc(sym=None, main_data=None, traversed=None):
    file_path = findSrcFile("nn/types.h")
    if not os.path.exists(file_path):
        print("nn/types.h missing, cannot continue.")
        return ""

    data, _m = traverseFile (file_path, sym, main_data, traversed)
    return data

def findSrcFile(pat):
    if len(pat) < 3:
        print ("Error: Cannot find empty string for path.")
        return pat

    p = Path(pat)
    if p.exists():
        return str(p)

    armcc = os.environ.get("ARMCC41INC")
    for base in include_paths + ([armcc] if armcc else []):
        candidate = Path(base) / pat
        #print(f"{pat}: {candidate}")
        if candidate.exists():
            return str(candidate)

    return pat

def traverseFile(pat, sym=None, main_data=None, traversed=None):
    if main_data is None:
        main_data = []

    content = []
    file_path = str(Path(findSrcFile(pat)).resolve())
    if len(file_path) == 0 or not os.path.exists(file_path):
        return "", main_data

    if traversed is None: traversed = set()
    if file_path in traversed:
        return "", main_data

    traversed.add(file_path)

    has_includes = False
    is_skipping = False
    is_ns_al = False
    is_main_data = True if main_data is None or len(main_data) == 0 else False
    if is_main_data:
        content.append('#define NON_MATCHING\n')

        if sym:
            content.append(f'// Context for {sym} in {file_path}\n')
            main_data.append(f'// Context for {sym} in {file_path}\n')
        else:
            content.append(f'// Context from {file_path}\n')
            main_data.append(f'// Context from {file_path}\n')
        
        for l in getTypeInc(sym, main_data, traversed): # to be called after anything is written to main_data.
            content.append(l)
    else:
        content.append(f"// File: {file_path}\n")

    with open(file_path, "r", encoding="shift-jis") as f:
        s = StringIO(f.read())
        for line in s:
            if is_skipping == True:
                continue

            if "#pragma once" in line:
                continue

            if not "#include" in line: # main append
                if is_main_data:
                    main_data.append(line)
                else:
                    content.append (line)
                if "namespace " in line:
                    is_ns_al = True
                continue
            
            if not '<' in line and not '>' in line:
                if not '\"' in line:
                    continue

            incl_path = ""
            match = re.search(r'"([^"]*)"|<([^>]*)>', line)
            if not match:
                continue

            incl_path = match.group(1) or match.group(2)

            included, _m = traverseFile (incl_path, sym, main_data, traversed)
            for incl_line in included:
                content.append(incl_line)
            content.append (f"// Includes End: {file_path}\n")
            has_includes = True

    if is_skipping == True and is_ns_al == True:
        if is_main_data:
            main_data.append ("Insert code here ...")
            main_data.append ("}")
        else:
            content.append ("}")

    return content, main_data

def genCtxs(path, symbol): # what is this again
    ctx_data, main_data = traverseFile(path, symbol)
    return "".join(ctx_data), "".join(main_data)
def gen_ctx(path):
    ctx_data, main_data = traverseFile(path)
    return "".join(ctx_data), "".join(main_data)

if __name__ == '__main__':
    import sys
    print("".join(genCtx(sys.argv[1])))
