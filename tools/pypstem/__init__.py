#!/usr/bin/env python3
import os
import subprocess
from tools.low.glob import *
from tools.pypstem.manCompiler import *
from tools.pypstem.callCompiler import *

# __init__.py: main build routine

compiler_path = None

# todo: add check to enforce specific formats for specific configs (cfg.py)
def getFileBuildPath(file):
    return getBuildPath() / file.relative_to(getProjDir()).with_suffix(".o")

def getMacroStr(macros):
    return "".join(f"-D{macro}={val or "1"} " for macro, val in macros.items())

def buildFile(file_in, file_out, add_flag, flag_asm, flag_cxx):
    flags = ""
    ext = os.path.splitext(file_in)[1]
    
    if not file_in.exists():
        fail (f"Bug: trying to build not existing source {file_in}")

    if "h" in ext:
        fail ("Why are you adding headers as source? (bad)")

    file_out.parent.mkdir(parents=True, exist_ok=True)

    if not "c" in ext:
        # asm
        flags += f" {add_flag} {cfg.flags_compile} {cfg.flags_compile_asm} -o {file_output} {file_input}"

        do_assemble(compiler_path, flags)
    else:
        # generic
        flags += "--cpp -c " if "cpp" in ext else "--c99 -c "
        flags += f" {add_flag} {cfg.flags_compile} {cfg.flags_compile_cxx} -o {file_out} {file_in}"

        do_compile(compiler_path, flags)
        

# ensure shift-jis
def convertFile(file):
    with open(file, 'rb') as f:
        data = f.read()

    try:
        data.decode('shift_jis')
        return
    except Exception:
        pass

    try:
        text = data.decode('utf-8')
        with open("/data/decomp/RedPepper/priv/test_out", 'wb') as f:
            f.write(text.encode('shift_jis'))
    except Exception as e:
        fail (f"Conversion failed for {file}: {e}")

def run():
    global compiler_path

    data_new = {}
    flags = ""

    # read file list
    data_old = None
    if os.path.exists(getListFile()):
        with open(getListFile(), "r") as f:
            data_old = {line.split()[0]: int(line.split()[1]) for line in f if line.strip()}

    check_wibo()

    # precreate include flags
    for src_path_name, src_data in cfg.modules.items():
        inc_path = getProjDir().joinpath(*src_path_name.split("/")).joinpath(*src_data["include_dir"].split("/"))
        flags += f"-I{inc_path} "
    
    flags += getMacroStr(cfg.macros)

    # iterate modules
    for src_path_name, src_data in cfg.modules.items():
        src_path = getProjDir().joinpath(*src_path_name.split("/")).joinpath(*src_data["source_dir"].split("/"))
        my_flags = flags
        my_flags_asm = None
        my_flags_cxx = None
        if src_data.get("flags"):
            my_flags_asm = src_data["flags"]
            my_flags_cxx = src_data["flags"]
        if src_data.get("flags_asm"):
            my_flags_asm += " "
            my_flags_asm += src_data["flags"]
        if src_data.get("flags_cxx"):
            my_flags_asm += " "
            my_flags_cxx += src_data["flags"]
        if src_data.get("macros"):
            my_flags += " "
            my_flags += getMacroStr(src_data["macros"])

        compiler_path = set_compiler(src_data["compiler"] if src_data.get("compiler") else cfg.compiler)

        # iterate specific files
        for file in src_path.rglob("**.*"):
            # check file extension
            file_str = str(file)
            if not file_str.split(".")[-1] in cfg.extensions:
                continue

            do_update = False
            timestamp = int(file.stat().st_mtime)
            if not data_old:
                do_update = True
            elif not file_str in data_old:
                do_update = True
            elif timestamp != data_old.get(file_str):
                do_update = True

            if do_update: # build it
                out_path = getFileBuildPath(file)
                convertFile(file)
                buildFile(file, out_path, my_flags, my_flags_asm, my_flags_cxx)

                if not out_path.exists():
                    fail_ex ("Output not found.", f"Looked for {out_path}")

            data_new[file_str] = timestamp

    if not data_new:
        echo ("No files found")

    with open(getListFile(), "w") as f:
        for file, date in data_new.items():
            f.write(f"{file} {date}\n")
