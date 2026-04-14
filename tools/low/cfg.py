#!/usr/bin/env python3
import os
import json

from tools.low.utilsPrint import *

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

flag_preinclude = None

# Switches
only_matching = False
allow_shifting = False
keep_objects = True
do_split = False

# Dict of macros
macros = {}

# helpers
def add_macro(str, val):
    macros[str] = val
def add_define(str):
    add_macro(str, "1")


def checkStrEntry(data, name):
    if name in data:
        if globals()[name]:
            globals()[name] += str(data.get(name))
        else:
            globals()[name] = str(data.get(name))
def checkIntEntry(data, name):
    if name in data:
        globals()[name] = int(data.get(name))
def checkBolEntry(data, name):
    if name in data:
        globals()[name] = bool(data.get(name))
        print (name)
def checkSetEntry(data, name):
    if data.get(name):
        if globals()[name]:
            globals()[name].extend(set(data.get(name)))
        else:
            globals()[name] = set(data.get(name))
def checkArrEntry(data, name):
    if name in data:
        if globals()[name]:
            globals()[name].extend(list(data.get(name)))
        else:
            globals()[name] = list(data.get(name))
def checkDctEntry(data, name):
    if name in data:
        if globals()[name]:
            globals()[name].update(dict(data.get(name)))
        else:
            globals()[name] = dict(data.get(name))

def readFile(path):
    if not path.exists():
        return

    global project_name, app_name, decompme_id, versions, modules, extensions

    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        fail_ex (f"Failed to read config!", e)

    checkStrEntry(data, "project_name")
    checkStrEntry(data, "app_name")
    checkIntEntry(data, "decompme_id")
    checkDctEntry(data, "versions")
    checkStrEntry(data, "default_version")
    checkStrEntry(data, "compiler")
    checkArrEntry(data, "flags_compile")
    checkArrEntry(data, "flags_compile_cxx")
    checkArrEntry(data, "flags_compile_asm")
    checkArrEntry(data, "flags_link")
    checkStrEntry(data, "flag_preinclude")
    checkDctEntry(data, "macros")
    checkSetEntry(data, "extensions")
    checkBolEntry(data, "only_matching")
    checkBolEntry(data, "allow_shifting")
    checkBolEntry(data, "keep_objects")
    checkBolEntry(data, "do_split")

    if data.get("preset_id"):
        fail ("Please rename preset_id to decompme_id!", False)
    my_modules = data.get("modules")
    if my_modules:
        if not modules:
            modules = {}
        for mod_id, mod_data in my_modules.items():
            if mod_data.get("disabled"):
                continue
            if mod_id in modules:
                for name, val in mod_data.items():
                    modules[mod_id][name] = val
            else:
                modules[mod_id] = mod_data
            if not mod_data.get("name"):
                fail (f"Module {mod_id} missing \'name\' entry")
            if not mod_data.get("source_dir"):
                modules[mod_id]["source_dir"] = "src"
            if not mod_data.get("include_dir"):
                modules[mod_id]["include_dir"] = "include"
            if mod_data.get("preset_id"):
                fail ("Please rename preset_id to decompme_id!", False)

assert_flag = True
def assertEntry(name):
    global assert_flag
    if globals()[name] is None:
        print (f"Missing: {name}")
        assert_flag = False

def assertCfg():
    assertEntry("project_name")
    assertEntry("versions")
    assertEntry("compiler")
    assertEntry("default_version")
    assertEntry("flags_compile")
    assertEntry("flags_link")

    if not modules or len(modules) <= 0:
        print ("config.json is missing modules.")

    if not assert_flag:
        fail ("config.json unusable, edit and try again.")

def read(verDir, dataDir):
    if not os.path.exists(str(dataDir / "config.json")):
        fail ("Missing config.json in data/.")

    readFile(dataDir / "config.json")
    readFile(verDir / "config.json")
    readFile(dataDir / "config.user.json")

    assertCfg()

