#!/usr/bin/env python3
import shutil
from tools.low.glob import *

curname = ""
curstatus = ""
progmax = 0
progidx = 0
def echo(str, end="\n"):
    print (f"\033[38;5;221m{str}\033[0m\033[K", end=end)
def clear_line():
    if is_silent: return
    print (' ' * shutil.get_terminal_size((80, 20)).columns, end='\r')
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
    clear_line()
    print (f"[{progidx}/{progmax}] \033[38;5;172m{curstatus}\033[38;2;150;75;0m{curname}\033[0m\033[K ...", end='\r')
def progress_upd_status(status):
    if is_silent: return
    progress_set_status(status)
    progress_print()

def getFileBuildPath(file):
    return getBuildPath() / file.relative_to(getProjDir()).with_suffix(".o")

def getMacroStr(macros):
    return "".join(f"-D{macro}={val or "1"} " for macro, val in macros.items())

