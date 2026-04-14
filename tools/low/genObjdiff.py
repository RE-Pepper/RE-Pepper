#!/usr/bin/env python3
import json
import sys
from colorama import Fore, Style
from elftools.elf.elffile import ELFFile
from elftools.elf.sections import SymbolTableSection

from tools.pypstem._utils import *
from tools.low.genContext import gen_ctx
from tools.low.getSymFile import read_sym_file, MapFmt
from tools.low.glob import *

# Generate objdiff.json

map_syms = set()
matching_syms = set()
def _doMatchingSyms():
    global matching_syms
    from tools.low.readSymMap import read_sym_file, MapFmt
    for sym in read_sym_file():
        symname = sym[MapFmt.Symbol]
        map_syms.add(symname)
        if sym[MapFmt.Rank] == 'O':
            matching_syms.add(symname)
_doMatchingSyms()

sym_file_list = {}
for file, syms in read_sym_file().items():
    if len(syms) < 3: continue
    for sym in syms[2:]:
        sym_file_list[sym] = {"module": syms[0], "preset_id": syms[1], "source_path": file}

def gen_objdiff(do_full_list=False):
    data = []
    modules_list = set()
    target_path = getBinCodeFile().with_suffix(".elf")
    base_path = getElfFile()

    for symbol in map_syms:
        name = sym[MapFmt.Symbol]
        module = None
        source_path = None
        preset_id = cfg.preset_id
        ctx_path = getProjDir() / cfg.flag_preinclude

        is_present = False
        is_complete = name in matching_syms

        if name in sym_file_list:
            is_present = True

            module = sym_file_list[name]["module"]
            preset_id = sym_file_list[name]["preset_id"]
            source_path = sym_file_list[name]["source_path"]

            if module and not module in modules_list:
                modules_list.add(module)

            ctx_path = getFileBuildPath(source_path).with_suffix(".ctx")
        elif not do_full_list:
            continue

        data.append(
                "    {\n"
               f'      "name": "{name}",\n'
               f'      "target_path": "{target_path}",\n'
        )
        if is_present:
            data.append(
               f'      "base_path": "{base_path}",\n'
            )
        data.append(
                '      "scratch": {\n'
                '        "platform": "n3ds",\n'
                '        "compiler": "outatime",\n'
               f'        "ctx_path": "{ctx_path}",\n'
        )
        if preset_id:
            data.append(
               f'        "preset_id": {preset_id},\n'
            )
        data.append(
               f'        "build_ctx": {"true" if is_present else "false"}\n'
        )
        data.append(
                '      },\n'
                '      "metadata": {\n'
               f'        "complete": {"true" if is_complete else "false"},\n'
        )
        if is_present:
            data.append(
               f'        "source_path": "{str(source_path)}",\n'
            )
        if module:
            data.append(
               f'        "progress_categories": ["{module}"],\n'
            )
        data.append(
                '        "auto_generated": false\n'
                '      }\n'
                '    }'
        )

    categories = []
    for mod in modules_list:
        categories.append(
            "    {\n"
           f"      \"name\": \"{mod}\",\n"
           f"      \"id\": \"{mod}\"\n"
            "    }"
        )

    objdiff_data = ""
    with open(Path(getProjDir()) / "data" / "template" / "objdiff.json", 'r') as f:
        objdiff_data = f.read()

    objdiff_data = objdiff_data.replace("###", ",\n".join(data))
    objdiff_data = objdiff_data.replace("$$$", ",\n".join(categories))

    with open(getJsonObjdiffFile(), 'w') as f:
        f.write(objdiff_data)

