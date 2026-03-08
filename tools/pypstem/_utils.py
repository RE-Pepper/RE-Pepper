#!/usr/bin/env python3
import shutil
from tools.low.glob import *

curname = ""
curstatus = ""
progmax = 0
progidx = 0
def progress_set(name, idx):
    global curname, progidx
    curname = name
    progidx = idx
def progress_set_type(status):
    global curstatus
    curstatus = status
def progress_set_max(max):
    global progmax
    progmax = max
def progress_print():
    if is_silent: return
    prog_line = ""
    if progmax > 0:
        prog_line += f"[{progidx}/{progmax}] "
    prog_line += f"\033[38;5;172m{curstatus}\033[38;2;150;75;0m{curname}\033[0m\033[K ..."
    print (prog_line, end='\r', flush=True)
def progress_upd_type(status):
    if is_silent: return
    progress_set_type(status)
    progress_print()

compiler_path = None
def set_compiler(path):
    global compiler_path
    compiler_path = Path(path)
def get_compiler():
    return compiler_path

def getFileBuildPath(file):
    return getBuildObjPath() / file.relative_to(getProjDir()).with_suffix(".o")

def getMacroStr(macros):
    return "".join(f"-D{macro}={val or "1"} " for macro, val in macros.items())

default_flags_comp = " --cpu=MPCore --fpmode=fast --apcs=/interwork "#--info=totals 
default_flags_comp_asm = "--diag_suppress=1608"
default_flags_comp_cxx = " --signed_chars --dollar --force_new_nothrow --no_rtti "


