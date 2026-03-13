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
    if not getMapFile().exists():
        fail ("Version not configured, cannot split.")

    ts_new = int(getMapFile().stat().st_mtime)

    def write_new():
        with open(getCfgMapFile(), "w") as f:
            f.write(f"{get_ver()} {ts_new}")

    if not getCfgMapFile().exists():
        write_new()
        return True

    ts_old = 0
    ver_old = 0
    with open(getCfgMapFile(), "r") as f:
        ver_old, ts_old = next(f).split()

    if get_ver() != ver_old:
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

        flags_asm = default_flags_comp
        flags_asm.extend(default_flags_comp_asm)
        flags_asm.append("--unaligned_access")
        if cfg.flags_compile:
            flags_asm.extend(cfg.flags_compile)
        if cfg.flags_compile_asm:
            flags_asm.extend(cfg.flags_compile_asm)
        ar_path = getSplitLibFile()
        flags_ar = ["--create", str(ar_path)]

        getSplitObjDir().mkdir(parents=True, exist_ok=True)

        for asm in getSplitAsmDir().rglob("*.s"):
            output = getSplitObjDir() / asm.with_suffix(".o").name

            asm_flags = flags_asm + ["-o", str(output), str(asm)]
            do_assemble(asm_flags)

            if asm.name.startswith("a"): # add to archive
                flags_ar.append(str(output))
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

