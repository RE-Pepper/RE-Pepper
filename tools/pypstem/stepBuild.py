#!/usr/bin/env python3
import os
import subprocess
from tools.low.glob import *
from tools.pypstem.manSetup import *
from tools.pypstem.callProcess import *
from tools.pypstem._utils import *

# __init__.py: main build routine

flags_asm = None
flags_cxx = None

default_flags_comp = "--cpu=MPCore --fpmode=fast --apcs=/interwork "#--info=totals 
default_flags_comp_asm = ""
default_flags_comp_cxx = "--signed_chars --dollar --force_new_nothrow --no_rtti "

# todo: add check to enforce specific formats for specific configs (cfg.py)
# todo: migrate old.py into this somehow (dont forget version checks!)

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
        flags += f"{flags_asm} {add_flag} -o {file_out} {file_in}"

        do_assemble(flags)
    else:
        # generic
        flags += "--c99" if ".c" == ext else " --cpp"
        flags += f" -c {flags_cxx} {add_flag} -o {file_out} {file_in}"

        do_compile(flags)

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

def exec_build():
    global flags_asm, flags_cxx

    data_new = {}
    flags = ""
    file_counter = 0

    progress_set("", 0)
    progress_set_type ("Preparing to build ...")

    # read file list
    data_old = None
    if os.path.exists(getListFile()):
        with open(getListFile(), "r") as f:
            data_old = {line.split()[0]: int(line.split()[1]) for line in f if line.strip()}

    check_wibo()

    # precreate flags
    for src_path_name, src_data in cfg.modules.items():
        inc_path = getProjDir().joinpath(*src_path_name.split("/")).joinpath(*src_data["include_dir"].split("/"))
        flags += f"-I{inc_path} "

    flags += getMacroStr(cfg.macros)
    if cfg.flag_preinclude:
        preinc_path = getProjDir().joinpath(*cfg.flag_preinclude.split("/"))
        flags += f"--preinclude={preinc_path} "
    if cfg.flag_diag:
        flags += cfg.flag_diag
        flags += " "
    flags += f"{default_flags_comp} {cfg.flags_compile} "
    flags_asm = f"{default_flags_comp_asm} {flags} {cfg.flags_compile_asm} "
    flags_cxx = f"{default_flags_comp_cxx} {flags} {cfg.flags_compile_cxx} "

    module_paths = {}
    module_files = {}
    # find max:
    data_len = 0
    for src_path_name, src_data in cfg.modules.items():
        src_path = getProjDir().joinpath(*src_path_name.split("/")).joinpath(*src_data["source_dir"].split("/"))
        module_paths[src_path_name] = src_path

        module_files[src_path_name] = set()
        for file in src_path.rglob("**.*"):
            # check file extension
            if not str(file).split(".")[-1] in cfg.extensions:
                continue

            module_files[src_path_name].add(file)
            data_len += 1
    progress_set_max(data_len)

    # iterate modules
    for src_path_name, src_data in cfg.modules.items():
        progress_set_type(f"{src_path_name}/")

        src_path = module_paths[src_path_name]
        my_flags = ""
        my_flags_asm = ""
        my_flags_cxx = ""
        val = src_data.get("flags")
        if val:
            my_flags_asm = val
            my_flags_cxx = val
        val = src_data.get("flags_asm")
        if val:
            my_flags_asm += " "
            my_flags_asm += val
        val = src_data.get("flags_cxx")
        if val:
            my_flags_asm += " "
            my_flags_cxx += val
        val = src_data.get("macros")
        if val:
            my_flags += getMacroStr(val)
            my_flags += " "

        set_compiler(setup_compiler(src_data.get("compiler") or cfg.compiler))

        # iterate specific files
        for file in sorted(module_files[src_path_name]):
            file_str = str(file)

            do_update = False
            timestamp = int(file.stat().st_mtime)
            out_path = getFileBuildPath(file)
            if not data_old: # .list file not exist
                do_update = True
            elif not out_path.exists(): # output not exist
                do_update = True
            elif not file_str in data_old: # file not in .list yet
                do_update = True
            elif timestamp != data_old.get(file_str): # timestamp mismatch
                do_update = True

            if do_update: # build it
                file_counter += 1
                progress_set(f"{file.name}", file_counter)
                progress_print()
            
                convertFile(file)
                buildFile(file, out_path, my_flags, my_flags_asm, my_flags_cxx)

                if not out_path.exists():
                    fail_ex ("Output not found.", f"Missing {out_path}")

            data_new[file_str] = timestamp
        line_category = ""
        if file_counter > 0:
            line_category += f"[{file_counter}]"
        line_category += f"[{len(module_files[src_path_name])}] {src_path_name}"
        echo (line_category)

    if not data_new:
        echo ("No files found")

    with open(getListFile(), "w") as f:
        for file, date in data_new.items():
            f.write(f"{file} {date}\n")
