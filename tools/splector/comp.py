#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path
from _settings import *
from splector._utils import *

gnuas = Path(os.environ["DEVKITARM"]) / "bin" / "arm-none-eabi-as"
gnunm = Path(os.environ["DEVKITARM"]) / "bin" / "arm-none-eabi-nm"
gnuobjcopy = Path(os.environ["DEVKITARM"]) / "bin" / "arm-none-eabi-objcopy"

class NmFmt(IntEnum):
    Address = 0
    Type = 1
    Symbol = 2

def run():
    print ("Recompiling ...")

    if not os.path.exists(getSplitAsmPath()):
        print (f"{getSplitAsmPath()} not found.")
        return

    subprocess.run([gnuas, "-mcpu=mpcore", "-mfpu=vfp", "-mfloat-abi=hard", "-o", getSplitObjPath(), getSplitAsmPath()])

    if not os.path.exists(getSplitObjPath()):
        print (f"{getSplitObjPath()} not found.")
        return

    print ("Patching ...")

    nm_out = str(subprocess.check_output([gnunm, getSplitObjPath()]))
    if sys.platform == 'win32': # Fix Newlines
        nm_out = nm_out.replace(r'\r\n', '\n')
    else:
        nm_out = nm_out.replace(r'\n', '\n')

    symlist = {}
    for line in nm_out.splitlines():
        line = line.split()
        if len(line) != 3:
            continue
        sym = str(line[NmFmt.Symbol])
        if "$$_$$" in sym:
            symlist[sym] = sym.replace("$$_$$", "::")

    objcopy_cmd = [gnuobjcopy]
    for old,new in symlist.items():
        objcopy_cmd.append("--redefine-sym")
        objcopy_cmd.append(f"{old}={new}")

    objcopy_cmd.append(getSplitObjPath())

    subprocess.run (objcopy_cmd)
