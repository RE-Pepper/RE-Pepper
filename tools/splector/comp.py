#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
from pathlib import Path
from _settings import *
from splector._utils import *

gnuar = Path(os.environ["DEVKITARM"]) / "bin" / "arm-none-eabi-ar"
gnuas = Path(os.environ["DEVKITARM"]) / "bin" / "arm-none-eabi-as"
gnunm = Path(os.environ["DEVKITARM"]) / "bin" / "arm-none-eabi-nm"
gnuobjcopy = Path(os.environ["DEVKITARM"]) / "bin" / "arm-none-eabi-objcopy"

class NmFmt(IntEnum):
    Address = 0
    Type = 1
    Symbol = 2

out_files = set()

def run():
    echo ("Splector mode: recompilation!")

    set_status ("Recompiling ")

    # in path exist?
    if not os.path.exists(getSplitInPath()):
        fail (f"{getSplitInPath()} not found.")

    # grab asm files
    in_files = getSplitInPath().glob("*.s")
    if not in_files:
        fail (f"{getSplitInPath()} is empty.")

    # create output path
    os.makedirs(getSplitOutPath(), exist_ok=True)

    for in_file in in_files:
        set_progress (in_file.name)
        print_progress()
    
        out_file = getSplitOutPath() / f"{in_file.stem}.o"
        subprocess.run([gnuas, "-mcpu=mpcore", "-mfpu=vfp", "-mfloat-abi=hard", "-I", getSplitInPath(), "-o", out_file, in_file])

        if not os.path.exists(out_file):
            fail (f"{out_file} not created.")

        out_files.add(out_file)

    set_status ("Patching ")

    for out_file in out_files:
        set_progress (out_file.name)
        print_progress()

        nm_out = str(subprocess.check_output([gnunm, out_file]))
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

        objcopy_cmd.append(out_file)

        subprocess.run (objcopy_cmd)

    upd_status ("Archiving ...")

    archive = getSplitDir() / f"{get_ver()}.a"
    
    ar_cmd = [gnuar, "rcs", archive]
    
    ar_cmd.extend(out_files)

    subprocess.run(ar_cmd)

    if not os.path.exists(archive):
        fail (f"{archive} not created.")
