#!/usr/bin/env python3
import shutil
import hashlib
from tools.low.glob import *
from tools.pypstem.defaultFlags import *

curname = ""
curstatus = ""
def progress_set(name):
    global curname
    curname = name
def progress_set_type(status):
    global curstatus
    curstatus = status
def progress_print():
    if isSilent(): return
    prog_line = ""
    prog_line += f"\033[38;5;172m{curstatus}\033[38;2;150;75;0m{curname}\033[0m\033[K ..."
    print (prog_line, end='\r', flush=True)
def progress_upd_type(status):
    if isSilent(): return
    progress_set_type(status)
    progress_print()

def getFileBuildPath(file):
    return getBuildObjPath() / file.relative_to(getProjDir()).with_suffix(".o")

def getMacroStr(macro, val):
    return f"-D{macro}={val or '1'}"
def getMacroArray(macros):
    if isinstance(macros, list):
        macros = dict.fromkeys(macros)
    return [getMacroStr(macro, val) for macro, val in macros.items()]

def getArrayHash(array):
    return hashlib.sha1(" ".join(map(str, array)).encode()).hexdigest()

def getModSrc(mod_path_name, mod_data):
    mod_subdir = mod_data.get("source_dir") or "."
    return getProjDir().joinpath(*str(mod_path_name).split("/")).joinpath(*str(mod_subdir).split("/"))
def getModInc(mod_path_name, mod_data):
    mod_subdir = mod_data.get("include_dir") or "."
    return getProjDir().joinpath(*str(mod_path_name).split("/")).joinpath(*str(mod_subdir).split("/"))

def isSymMapDiff():
    if not getMapFile().exists():
        fail ("Version not configured, cannot split.")

    ts_new = int(getMapFile().stat().st_mtime)

    def write_new():
        with open(getCfgMapFile(), "w") as f:
            f.write(f"{getVersion()} {ts_new}")

    if not getCfgMapFile().exists():
        write_new()
        return True

    ts_old = 0
    ver_old = 0
    with open(getCfgMapFile(), "r") as f:
        ver_old, ts_old = next(f).split()

    if getVersion() != ver_old:
        write_new()
        return True
    if int(ts_old) != ts_new:
        write_new()
        return True

    return False

