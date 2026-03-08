#!/usr/bin/env python3
import os
import subprocess
from tools.low.glob import *
from tools.pypstem.manSetup import *
from tools.pypstem.callProcess import *
from tools.pypstem._utils import *

# __init__.py: main build routine

flags_asm = ""
flags_cxx = ""

# todo: add check to enforce specific formats for specific configs (cfg.py)

def buildFile(file_in, file_out, add_flag, flag_asm, flag_cxx):
    flags = ""
    
    if not file_in.exists():
        fail (f"Bug: trying to build not existing source {file_in}")

    if "h" in file_in.suffix:
        fail ("Why are you adding headers as source? (bad)")

    file_out.parent.mkdir(parents=True, exist_ok=True)

    if not "c" in file_in.suffix:
        # asm
        flags += f"{flags_asm} {add_flag} -o {file_out} {file_in}"

        do_assemble(flags)
    else:
        # generic
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

def exec_build(add_macros=None):
    global flags_asm, flags_cxx

    if not cfg.modules or len(cfg.modules) <= 0:
        echo ("No modules are specified, nothing to build.")
        return

    data_new = {}
    data_new_names = set()
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
    # includes
    for mod_path_name, mod_data in cfg.modules.items():
        if not mod_data.get("include_dir"):
            continue
        inc_path = getProjDir().joinpath(*str(mod_path_name).split("/")).joinpath(*mod_data.get("include_dir").split("/"))
        flags_cxx += f" -I{inc_path} "
    # macros
    flags_cxx += getMacroStr(cfg.macros)
    flags_cxx += f" -DVERSION={getVersion().upper()}"
    if add_macros:
        if isinstance(add_macros, dict):
            flags_cxx += getMacroStr(add_macros)
        elif sinstance(add_macros, list):
            flags_cxx += getMacroStr(dict.fromkeys(add_macros))
    # preinclude
    if cfg.flag_preinclude:
        preinc_path = getProjDir().joinpath(*str(cfg.flag_preinclude).split("/"))
        flags_cxx += f" --preinclude={preinc_path} "
    # diagnosis
    if cfg.flag_diag:
        flags += cfg.flag_diag
        flags += " "
    # main
    flags += f" {default_flags_comp} {cfg.flags_compile} "
    flags_asm += f" {default_flags_comp_asm} {flags} "
    if cfg.flags_compile_asm:
        flags_asm += f"{cfg.flags_compile_asm} "
    flags_cxx += f" {default_flags_comp_cxx} {flags} "
    if cfg.flags_compile_cxx:
        flags_cxx += f"{cfg.flags_compile_cxx} "

    module_paths = {}
    module_files = {}
    # find max:
    data_len = 0
    for mod_path_name, mod_data in cfg.modules.items():
        mod_dir = mod_data.get("source_dir") or "."
        mod_path = getProjDir().joinpath(*str(mod_path_name).split("/")).joinpath(*str(mod_dir).split("/"))
        module_paths[mod_path_name] = mod_path

        module_files[mod_path_name] = set()
        for file in mod_path.rglob("**.*"):
            # check file extension
            if not file.suffix.lstrip(".") in cfg.extensions:
                continue

            module_files[mod_path_name].add(file)
            data_len += 1
    progress_set_max(data_len)

    # iterate modules
    for mod_path_name, mod_data in cfg.modules.items():
        progress_set_type(f"{mod_path_name}/")

        mod_ar_name = f"lib{mod_data.get("name")}.a"
        mod_ar_file = getBuildLibPath() / mod_ar_name
        mod_ar_arg_add = f"-r {str(mod_ar_file)}"
        mod_ar_arg_rem = f"-d {str(mod_ar_file)}"
        mod_ar_do_add = False
        mod_ar_do_rem = False

        mod_path = module_paths[mod_path_name]
        my_flags = ""
        my_flags_asm = ""
        my_flags_cxx = ""
        val = mod_data.get("flags")
        if val:
            my_flags_asm = val
            my_flags_cxx = val
        val = mod_data.get("flags_asm")
        if val:
            my_flags_asm += " "
            my_flags_asm += val
        val = mod_data.get("flags_cxx")
        if val:
            my_flags_asm += " "
            my_flags_cxx += val
        val = mod_data.get("macros")
        if val:
            my_flags += getMacroStr(val)
            my_flags += " "

        set_compiler(setup_compiler(mod_data.get("compiler") or cfg.compiler))

        # iterate specific files
        for file in sorted(module_files[mod_path_name]):
            file_str = str(file.relative_to(getProjDir()))

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
                    fail_ex ("Output not found.", f"Missing {str(out_path)}")
                else:
                    mod_ar_arg_add += " "
                    mod_ar_arg_add += str(out_path)
                    mod_ar_do_add = True

            data_new[file_str] = timestamp
            data_new_names.add(file.name)

        for old_file, _ in data_old.items():
            old_name = Path(old_file).name
            if not old_name in data_new_names:
                mod_ar_arg_rem += str(old_name)
                mod_ar_arg_rem += " "
                mod_ar_do_rem = True

        line_category = ""
        if file_counter > 0:
            line_category += f"[{file_counter}]"
        line_category += f"<{len(module_files[mod_path_name])}> {mod_data.get("name")}"

        if mod_ar_do_add:
            echo (f"{line_category}: Archive add", "\r")
            do_archive(mod_ar_arg_add)
        if mod_ar_do_rem:
            echo (f"{line_category}: Archive remove", "\r")
            do_archive(mod_ar_arg_rem)

        if mod_ar_do_add or mod_ar_do_rem:
            echo (f"{line_category}: Done")
        else:
            echo (f"{line_category}: Unchanged")

    if not data_new:
        echo ("No files found")

    with open(getListFile(), "w") as f:
        for file, date in data_new.items():
            f.write(f"{file} {date}\n")
