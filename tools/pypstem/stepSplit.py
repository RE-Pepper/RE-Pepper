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

    if not getMapFile().exists():
        fail ("Version not configured, cannot split.")

    ts_new = int(getMapFile().stat().st_mtime)

    def write_new():
        path_mapcfg = str(getCfgMapFile().relative_to(getProjDir()))
        with open(path_mapcfg, "w") as f:
            f.write(f"{path_mapcfg} {ts_new}")

    if not store_file.exists():
        write_new()
        return True

    ts_old = 0
    with open(store_file, "r") as f:
        map_old, ts_old = next(f).split()

    if str(Path(map_old).relative_to(getProjDir())) != str(getMapFile().relativeTo(getProjDir())):
        write_new()
        return True
    if int(ts_old) != ts_new:
        write_new()
        return True

    return False

def exec_split(clear=False):
    if clear or isSymMapDiff() or not getSplitLibFile().exists() or (getSplitAsmDir().exists() and not cfg.keep_objects):
        echo ("Splitting assembly")

        if getSplitLibFile().exists():
            getSplitLibFile().unlink()
        if getSplitAsmDir().exists():
            shutil.rmtree(getSplitAsmDir(), ignore_errors=True)
        if getSplitObjDir().exists():
            shutil.rmtree(getSplitObjDir(), ignore_errors=True)
        
        splector.split.run()

        if not getSplitAsmDir().exists():
            fail ("Splits are missing.")

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

        getSplitObjDir().mkdir(parents=True, exist_ok=True)

        for asm in getSplitAsmDir().rglob("*.s"):
            output = getSplitObjDir() / asm.with_suffix(".o").name

            asm_flags = f"{flags_asm} -o {str(output)} {asm}"
            do_assemble(asm_flags)

            if asm.name.startswith("a"): # add to archive
                flags_ar += " "
                flags_ar += str(output)
            else: # special file, move to build folder
                output.rename(getSplitPath() / output.name)

        echo ("Archiving splits")

        getBuildLibPath().mkdir(parents=True, exist_ok=True)
        do_archive(flags_ar)

        if not cfg.keep_objects:
            shutil.rmtree(getSplitAsmDir(), ignore_errors=True)
            shutil.rmtree(getSplitObjDir(), ignore_errors=True)
    else:
        echo ("Assembly up to date")

