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

def exec_split(clear=False):
    if clear or isSymMapDiff() or not getSplitLibFile().exists() or (getSplitAsmDir().exists() and not cfg.keep_objects):
        echo ("Splitting assembly (may take a few minutes)")

        if getSplitLibFile().exists():
            getSplitLibFile().unlink()
        if getSplitAsmDir().exists():
            shutil.rmtree(getSplitAsmDir(), ignore_errors=True)
        if getSplitObjDir().exists():
            shutil.rmtree(getSplitObjDir(), ignore_errors=True)
        
        splector.split.run()

        if not getSplitAsmDir().exists():
            fail ("Splits are missing.")

        echo ("Recompiling splits")

        setup_compiler(cfg.compiler)

        flags_asm = default_flags_comp
        flags_asm.extend(default_flags_comp_asm)
        if cfg.flags_compile:
            flags_asm.extend(cfg.flags_compile)
        if cfg.flags_compile_asm:
            flags_asm.extend(cfg.flags_compile_asm)

        getSplitObjDir().mkdir(parents=True, exist_ok=True)

        for asm in getSplitAsmDir().rglob("*.s"):
            output = getSplitObjDir() / asm.with_suffix(".o").name
            echo (f"> {output.name} <", "\r")

            asm_flags = flags_asm + ["-o", str(output), str(asm)]
            do_assemble(asm_flags)

            if not asm.name.startswith("a"):
                output.replace(getSplitPath() / output.name)

        echo ("Archiving splits")

        ar_path = str(getSplitLibFile())
        getBuildLibPath().mkdir(parents=True, exist_ok=True)
        for obj in getSplitObjDir().rglob("*.o"):
            echo (f"> {obj.name} <", "\r")
            flags_ar = ["-rcn", ar_path, str(obj)]
            do_archive(flags_ar)

        flags_ar = ["-s", ar_path]
        do_archive(flags_ar)

        if not cfg.keep_objects:
            shutil.rmtree(getSplitAsmDir(), ignore_errors=True)
            shutil.rmtree(getSplitObjDir(), ignore_errors=True)
    else:
        echo ("Assembly up to date")

