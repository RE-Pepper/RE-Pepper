#!/usr/bin/env python3
import os
import shutil
import tools.splector as splector
import tools.splector.split
from tools.pypstem._utils import *
from tools.pypstem.callProcess import *
from tools.pypstem.manSetup import setup_compiler
from tools.low.glob import *

# TODO: also resplect if csv map changed

def isSymMapDiff():
    store_file = getDataDir() / ".map"

    def write_new(path, ts):
        with open(store_file, "w") as f:
            f.write(f"{str(path)} {ts}")

    if not getMapFile().exists():
        fail ("Version not configured, cannot split.")

    ts_new = int(getMapFile().stat().st_mtime)

    if not store_file.exists():
        write_new(getMapFile(), ts_new)
        return True

    ts_old = 0
    with open(store_file, "r") as f:
        map_old, ts_old = next(f).split()

    write_new(getMapFile(), ts_new)

    if map_old != str(getMapFile()):
        return True
    if int(ts_old) != ts_new:
        return True

    return False

def exec_split(clear=False):
    echo ("Splitting assembly")

    if clear or isSymMapDiff() or not getSplitLibFile().exists() or getSplitPath().exists():
        if clear and getSplitLibFile().exists():
            getSplitLibFile().unlink()
        
        splector.split.run()

        if not getSplitAsmDir().exists():
            fail ("Split list missing.")

        echo ("Compiling split")

        set_compiler(setup_compiler(cfg.compiler))

        flags_asm = f"{default_flags_comp} {default_flags_comp_asm} --unaligned_access "
        if cfg.flags_compile:
            flags_asm += cfg.flags_compile
            flags_asm += " "
        if cfg.flags_compile_asm:
            flags_asm += cfg.flags_compile_asm
            flags_asm += " "
        ar_path = getSplitLibFile()
        flags_ar = f"--create {str(ar_path)}"

        for asm in getSplitAsmDir().rglob("*.s"):
            output = getSplitObjDir() / asm.with_suffix(".o")

            do_assemble(f"{flags_asm} -o {str(output)} {asm}")

            if asm.name.startswith("a"): # add to archive
                flags_ar += " "
                flags_ar += str(output)
            else: # special file, move to build folder
                output.rename(getBuildObjPath() / output.name)

        echo ("Archiving splits")

        getBuildLibPath().mkdir(parents=True, exist_ok=True)
        do_archive(flags_ar)

        shutil.rmtree(getSplitPath(), ignore_errors=True)

