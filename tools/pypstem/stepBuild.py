#!/usr/bin/env python3
import os
import json
import shlex
import subprocess
from tools.low.readElfSym import *
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
    
    flags_add = ["-o", file_out, "--depend", file_out.with_suffix(".d"), file_in]

    if not "c" in file_in.suffix:
        flags = flags_asm + flags_add
        do_assemble(flags)
    else:
        flags = flags_cxx + ["-c"] + flags_add
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

def fixDependFile(file):
    dep_data = None
    with open(file, "r") as f:
        dep_data = f.read().splitlines()

    for li in range(len(dep_data)):
        line = dep_data[li].replace(": ", " ") # remove ": "
        row = shlex.split(line)
        src_f = Path(row[1])
        ts = 0
        if src_f.exists():
            ts = int(src_f.stat().st_mtime)

        dep_data[li] = f"{line} \"{ts}\""

    with open(file, "w") as f:
        f.write("\n".join(dep_data))

def areDependsNew(file):
    dep_data = None
    with open(file, "r") as f:
        dep_data = f.read().splitlines()

    for line in dep_data:
        row = shlex.split(line)

        if len(row) != 3:
            return True

        src_f = Path(row[1])
        ts_o = int(row[2])

        if not src_f.exists():
            return True
        ts_n = int(src_f.stat().st_mtime)
        if ts_n != ts_o:
            return True

    # no mismatches
    return False

def exec_build():
    echo ("Building modules")

    global flags_asm, flags_cxx
    if not cfg.modules or len(cfg.modules) <= 0:
        echo ("No modules are specified, nothing to build.")
        return

    data_new_names = set()
    has_update = False

    progress_set("")
    progress_set_type ("Preparing to build ...")

    flags_old = None
    if getCfgFlagsFile().exists():
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

    json_syms = {}
    if getCfgSymsFile().exists():
        with open(getCfgSymsFile(), "r") as f:
            json_syms = json.load(f)

    if getCfgFlagsTFile().exists():
        getCfgFlagsTFile().unlink()

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
        base_flags_cxx.extend(cfg.flags_compile_cxx)
    if cfg.flag_preinclude:
        preinc_path = getProjDir() / Path(cfg.flag_preinclude)
        base_flags_cxx.append(f"--preinclude={preinc_path}")

    # find files and note length

    module_paths = {}
    module_files = {}

    for mod_path_name, mod_data in cfg.modules.items():
        mod_path = getModSrc(mod_path_name, mod_data)
        module_paths[mod_path_name] = mod_path

        mod_extensions = cfg.extensions
        if "extensions" in mod_data:
            mod_extensions = mod_data.get("extensions")

        module_files[mod_path_name] = set()
        for file in mod_path.rglob("*"):
            if not file.is_file():
                continue
            ext_name = file.suffix.lstrip(".")
        
            # check file extension
            if not ext_name or len(ext_name) < 1 or not ext_name in mod_extensions:
                continue

            module_files[mod_path_name].add(file)

    # iterate modules
    for mod_path_name, mod_data in cfg.modules.items():
        progress_set_type(f"{mod_path_name}/")

        obj_new_list = set()
    
        mod_ar_name = f"lib{mod_data.get("name")}.a"
        mod_ar_file = getBuildLibPath() / mod_ar_name

        flags_cxx = base_flags_cxx[:]
        flags_asm = base_flags_asm[:]
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
        val = mod_data.get("compiler")
        if val:
            setup_compiler(val)

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
        if not getCfgSymsFile().exists():
            force_update = True
        if not mod_ar_file.exists():
            force_update = True

        # iterate files
        for file in sorted(module_files[mod_path_name]):
            file_str = os.path.relpath(file, getProjDir())

            do_update = False
            out_path = getFileBuildPath(file)
            dep_path = getFileBuildPath(file).with_suffix(".d")
            if force_update:
                do_update = True
            elif not out_path.exists(): # output not exist
                do_update = True
            elif not dep_path.exists(): # dependency doesnt exist
                do_update = True
            elif areDependsNew(dep_path): # timestamp mismatch
                do_update = True

            if do_update: # build it
                has_update = True

                # set progress
                progress_set(f"{file.name}")
                progress_print()

                # build it
                convertFile(file)
                buildFile(file, out_path)

                # post process
                if not out_path.exists():
                    fail_ex ("Output not found.", f"Missing {str(out_path)}")

                fixDependFile(dep_path)
                # add to list
                obj_new_list.add(out_path)
            data_new_names.add(file.name)

            # write down symbols in .syms
            if not str(getBuildPath()) in str(file):
                if file_str in json_syms:
                    del json_syms[file_str]
                json_syms[file_str] = []
                for sym in read_elfsym(out_path):
                    if sym[ElfSymFmt.Symbol] in json_syms[file_str]:
                        continue
                    json_syms[file_str].append(sym[ElfSymFmt.Symbol])

        did_delete = False
        # check for deleted files
        if data_new_names and mod_ar_file.exists():
            build_dir = getBuildObjPath() / mod_path_name
            # find all dependency files
            for file in build_dir.rglob("*.d"):
                # open dependency file
                with open(file, "r") as f:
                    line = f.read().splitlines()[0]
                    row = shlex.split(line)
                    if len(row) != 3:
                        continue

                    if Path(row[1]).name in data_new_names:
                        continue
                    if Path(row[0]).exists():
                        continue

                    ar_arg = ["-dcs", str(mod_ar_file), "--diag_suppress=6831", str(Path(row[0]).name)]
                    do_archive(ar_arg)
                    did_delete = True

        # prebuild module string
        line_category = ""
        line_category += f"<{len(module_files[mod_path_name])}> {mod_data.get("name")}"

        # append to archive
        if len(obj_new_list) > 0:
            # Build .via file
            with open(getBuildViaFile(), "w") as f:
                for obj in obj_new_list:
                    f.write(str(obj))
                    f.write(" ")

            echo (f"{line_category}: Compressing", "\r")
            ar_arg = ["-rsc", str(mod_ar_file), f"--via={str(getBuildViaFile())}"]
            do_archive(ar_arg)


        # write flags down
        with open(getCfgFlagsTFile(), "a") as f:
            f.write(f"{mod_path_name} {new_flags_cxx_hash}\n")
            f.write(f"{mod_path_name} {new_flags_asm_hash}\n")

        # clean / report
        if len(obj_new_list) <= 0 and not did_delete:
            echo (f"{line_category}: Unchanged")
            continue

        if len(obj_new_list) > 0 and not cfg.keep_objects:
            echo (f"{line_category}: Cleaning", "\r")
            for f in obj_new_list:
                f.unlink()
            shutil.rmtree(getBuildObjPath() / os.path.relpath(mod_path, getProjDir()).split(os.sep)[0])

        echo (f"{line_category}: Done")

    getCfgFlagsTFile().replace(getCfgFlagsFile())

    if getBuildViaFile().exists():
        getBuildViaFile().unlink()

    with open(getCfgSymsFile(), "w") as f:
        json.dump(json_syms, f)

    return has_update
