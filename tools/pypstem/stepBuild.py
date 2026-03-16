#!/usr/bin/env python3
import os
import subprocess
from tools.low.glob import *
from tools.pypstem.manSetup import *
from tools.pypstem.callProcess import *
from tools.pypstem._utils import *

# __init__.py: main build routine

flags_asm = []
flags_cxx = []

# todo: add check to enforce specific formats for specific configs (cfg.py)

def buildFile(file_in, file_out):
    if not file_in.exists():
        fail (f"Bug: trying to build not existing source {file}")

    if "h" in file_in.suffix:
        fail ("Why are you adding headers as source? (bad)")

    file_out.parent.mkdir(parents=True, exist_ok=True)

    if not "c" in file_in.suffix:
        flags = flags_asm + ["-o", file_out, file_in]
        do_assemble(flags)
    else:
        flags = flags_cxx + ["-c", "-o", file_out, file_in]
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
        with open(file, 'wb') as f:
            f.write(text.encode('shift_jis'))
    except Exception as e:
        fail (f"Conversion failed for {file}: {e}")

def exec_build():
    echo ("Building modules")

    global flags_asm, flags_cxx

    if not cfg.modules or len(cfg.modules) <= 0:
        echo ("No modules are specified, nothing to build.")
        return

    data_new = {}
    data_new_names = set()
    file_counter = 0

    progress_set("", 0)
    progress_set_type ("Preparing to build ...")

    # read file list
    data_old = None
    if os.path.exists(getCfgListFile()):
        data_old = {}
        with open(getCfgListFile(), "r") as f:
            for line in f:
                row = line.split()
                if len(row) != 2:
                    echo ("data/.files is corrupt, rebuilding.")
                    getCfgListFile().unlink()
                    break

                data_old[row[0]] = int(row[1])
    flags_old = None
    if os.path.exists(getCfgFlagsFile()):
        flags_old = {}
        with open(getCfgFlagsFile(), "r") as f:
            for line in f:
                row = line.split()
                if len(row) != 2:
                    echo ("data/.flags is corrupt, rebuilding.")
                    getCfgFlagsFile().unlink()
                    break

                if row[0] in flags_old:
                    flags_old[f"{row[0]}_s"] = row[1]
                else:
                    flags_old[row[0]] = row[1]

    if getCfgFlagsTFile().exists():
        getCfgFlagsTFile().unlink()

    getCfgSymsFile().unlink()

    # precreate flags
    base_flags = []
    base_flags_cxx = []
    base_flags_asm = []
    # includes
    for mod_path_name, mod_data in cfg.modules.items():
        if not mod_data.get("include_dir"):
            continue
        inc_path = getModInc(mod_path_name, mod_data)
        base_flags_cxx.append(f"-I{inc_path}")
    # macros
    base_flags_cxx.append(getMacroStr("VERSION", getVersion().upper()))
    base_flags_cxx.extend(getMacroArray(cfg.macros))
    # main
    base_flags.extend(default_flags_comp)
    base_flags.extend(cfg.flags_compile)
    base_flags_asm.extend(base_flags)
    base_flags_asm.extend(default_flags_comp_asm)
    base_flags_cxx.extend(base_flags)
    base_flags_cxx.extend(default_flags_comp_cxx)

    if cfg.flags_compile_asm:
        base_flags_asm.extend(cfg.flags_compile_asm)
    if cfg.flags_compile_cxx:
        base_flags_asm.extend(cfg.flags_compile_cxx)

    # find files and note length

    module_paths = {}
    module_files = {}
    data_len = 0

    for mod_path_name, mod_data in cfg.modules.items():
        mod_path = getModSrc(mod_path_name, mod_data)
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

        obj_new_list = set()
    
        mod_ar_name = f"lib{mod_data.get("name")}.a"
        mod_ar_file = getBuildLibPath() / mod_ar_name

        mod_path = module_paths[mod_path_name]
        flags_cxx = base_flags_cxx
        flags_asm = base_flags_asm
        val = mod_data.get("flags")
        if val:
            flags_asm.extend(val)
            flags_cxx.extend(val)
        val = mod_data.get("flags_asm")
        if val:
            flags_asm.extend(val)
        val = mod_data.get("flags_cxx")
        if val:
            flags_cxx.extend(val)
        val = mod_data.get("macros")
        if val:
            flags_cxx.extend(getMacroArray(val))

        setup_compiler(mod_data.get("compiler"))

        old_flags_cxx = None
        old_flags_asm = None
        if flags_old:
            old_flags_cxx = flags_old.get(mod_path_name)
            old_flags_asm = flags_old.get(f"{mod_path_name}_s")

        new_flags_cxx_hash = getArrayHash(flags_cxx)
        new_flags_asm_hash = getArrayHash(flags_asm)

        force_update = False
        if (new_flags_cxx_hash != old_flags_cxx) or (new_flags_asm_hash != old_flags_asm):
            force_update = True # flags mismatch

        # iterate files
        for file in sorted(module_files[mod_path_name]):
            file_str = os.path.relpath(file, getProjDir())

            do_update = False
            timestamp = int(file.stat().st_mtime)
            out_path = getFileBuildPath(file)
            if force_update:
                do_update = True
            elif not data_old: # .files file not exist
                do_update = True
            elif not out_path.exists(): # output not exist
                do_update = True
            elif not file_str in data_old: # file not in .files yet
                do_update = True
            elif timestamp != data_old.get(file_str): # timestamp mismatch
                do_update = True

            if do_update: # build it
                file_counter += 1
                progress_set(f"{file.name}", file_counter)
                progress_print()
            
                convertFile(file)
                buildFile(file, out_path)

                if not out_path.exists():
                    fail_ex ("Output not found.", f"Missing {str(out_path)}")
                else:
                    ar_arg = ["-rn", str(mod_ar_file), str(out_path)]
                    do_archive(ar_arg)
                    obj_new_list.add(out_path)

            data_new[file_str] = timestamp
            data_new_names.add(file.name)

        did_delete = False
        # check for deleted files
        if data_old and data_new_names:
            for old_file, _ in data_old.items():
                if not str(Path(mod_path_name) / mod_data.get("source_dir")) in old_file:
                    continue
                if Path(old_file).name in data_new_names:
                    continue
                ar_arg = ["-ds", str(mod_ar_file), "--diag_suppress=6831", str(Path(old_file).with_suffix(".o").name)]
                do_archive(ar_arg)
                did_delete = True

        # write flags down
        with open(getCfgFlagsTFile(), "a") as f:
            f.write(f"{mod_path_name} {new_flags_cxx_hash}\n")
            f.write(f"{mod_path_name} {new_flags_asm_hash}\n")

        # prebuild module string
        line_category = ""
        if file_counter > 0:
            line_category += f"[{file_counter}]"
        line_category += f"<{len(module_files[mod_path_name])}> {mod_data.get("name")}"

        # clean / report
        if len(obj_new_list) <= 0 and not did_delete:
            echo (f"{line_category}: Unchanged")
            continue

        ar_arg = ["-s", str(mod_ar_file)]
        do_archive(ar_arg)

        if len(obj_new_list) > 0 and not cfg.keep_objects:
            echo (f"{line_category}: Cleaning", "\r")
            for f in obj_new_list:
                f.unlink()
            shutil.rmtree(getBuildObjPath() / os.path.relpath(mod_path, getProjDir()).split(os.sep)[0])

        echo (f"{line_category}: Done")

    if not data_new:
        echo ("No files found")

    getCfgFlagsTFile().replace(getCfgFlagsFile())

    with open(getCfgListFile(), "w") as f:
        for file, time in data_new.items():
            f.write(f"{file} {time}\n")
