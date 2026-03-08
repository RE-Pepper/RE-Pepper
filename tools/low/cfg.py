#!/usr/bin/env python3
import os
import json

# GLOBAL CONFIG

# Name of the Project (Project.axf)
project_name = None

# Name of the binary (from exh.bin in hex viewer, only first 6 bytes)
# if undefined, exh.bin cannot be reviewed
app_name = None

# Game ID from decomp.me
# if undefined, tools/upload wont work
decompme_id = None

# Dict of versions + sha256sum
versions = None

# Default version to use
default_version = None

# Fallback compiler version.
# if undefined, and a module is missing compiler, error.
compiler = None

# Module objects.
# Example:
# "lib/ctrsdk": {
#   "name":        "ctrsdk"  # required for archive name (libctrsdk.a)
#   "source_dir":  "src"     # defaults fo "src"
#   "include_dir": "include" # defaults to "include"
#   "compiler":    "4.1/791" # defaults to fallback compiler, error if nowhere
#   "flags":       "-c"      # additional flags (base)
#   "flags_asm":   "-c"      # additional flags (add for asm)
#   "flags_cxx":   "-c"      # additional flags (add for cxx)
#   "decompme_id": 8         # defaults to main, tools/upload unusable if nowhere
# }
modules = {}

# Extension of source files. Can be left as default
extensions = set(["cpp", "c", "s"])

#  Error if missing any flags
# Full flags for compiling (base)
flags_compile = None
# Full flags for compiling C/C++
flags_compile_cxx = None
# Full flags for compiling ASM
flags_compile_asm = None
# Full flags for linking
flags_link = None

# Optional flag for preinclude
flag_preinclude = None
flag_diag = None

# Dict of macros
macros = {}

# helpers
def add_macro(str, val):
    macros[str] = val
def add_define(str):
    add_macro(str, "1")



def _fail(str):
    print (f"\033[38;5;196mError: {str}\033[0m\033[K")
    exit(1)

def checkStrEntry(data, name):
    my_entry = data.get(name)
    if my_entry:
        globals()[name] = str(my_entry)
def checkIntEntry(data, name):
    my_entry = data.get(name)
    if my_entry:
        globals()[name] = int(my_entry)
def checkSetEntry(data, name):
    my_entry = data.get(name)
    if my_entry:
        if globals()[name]:
            globals()[name].extend(set(my_entry))
        else:
            globals()[name] = set(my_entry)
def checkDctEntry(data, name):
    my_entry = data.get(name)
    if my_entry:
        if globals()[name]:
            globals()[name].update(dict(my_entry))
        else:
            globals()[name] = dict(my_entry)

def readFile(path):
    global project_name, app_name, decompme_id, versions, modules, extensions

    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        _fail (f"Failed to read config: {e}")

    checkStrEntry(data, "project_name")
    checkStrEntry(data, "app_name")
    checkIntEntry(data, "decompme_id")
    checkDctEntry(data, "versions")
    checkStrEntry(data, "default_version")
    checkStrEntry(data, "compiler")
    checkStrEntry(data, "flags_compile")
    checkStrEntry(data, "flags_compile_cxx")
    checkStrEntry(data, "flags_compile_asm")
    checkStrEntry(data, "flags_link")
    checkStrEntry(data, "flag_preinclude")
    checkStrEntry(data, "flag_diag")
    checkSetEntry(data, "macros")
    checkSetEntry(data, "extensions")

    my_modules = data.get("modules")
    if my_modules:
        if not modules:
            modules = {}
        for my_src_name, my_src_cfg in my_modules.items():
            if my_src_name in modules:
                for name, val in my_src_cfg.items():
                    modules[my_src_name][name] = val
            else:
                modules[my_src_name] = my_src_cfg
            if not modules[my_src_name].get("name"):
                _fail (f"Module {my_src_name} missing \'name\' entry")
            if not modules[my_src_name].get("source_dir"):
                modules[my_src_name]["source_dir"] = "src"
            if not modules[my_src_name].get("include_dir"):
                modules[my_src_name]["include_dir"] = "include"

assert_flag = True
def assertEntry(name):
    global assert_flag
    if globals()[name] is None:
        print (f"Missing: {name}")
        assert_flag = False

def assertCfg():
    assertEntry("project_name")
    assertEntry("app_name")
    assertEntry("versions")
    assertEntry("compiler")
    assertEntry("default_version")
    assertEntry("flags_compile")
    assertEntry("flags_link")

    if not modules or len(modules) <= 0:
        print ("config.json is missing modules.")

    if not assert_flag:
        _fail ("config.json is not complete, edit and try again.")

def read(verDir, dataDir):
    if not os.path.exists(str(dataDir / "config.json")):
        _fail ("Missing config.json in data/.")

    readFile(str(dataDir / "config.json"))
    
    if not os.path.exists(str(verDir / "config.json")):
        assertCfg()
        return

    readFile(str(verDir / "config.json"))

    assertCfg()

