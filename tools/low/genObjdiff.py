#!/usr/bin/env python3
import json
import sys
from colorama import Fore, Style
from elftools.elf.elffile import ELFFile
from elftools.elf.sections import SymbolTableSection

from tools.low.genContext import gen_ctx
from tools.low.glob import *

# Generate objdiff.json (WNIP)

def get_paths_for (file):
    paths = get_paths()

    for src, obj in paths:
        if file.rsplit('.', 1)[0] in obj or file.rsplit('.', 1)[0] in src:
            return src, obj

    return "",""

def makeCtxFile(src, obj):
    out = obj.rsplit('.', 1)[0] + '.ctx'

    data, main = genCtx(src)
    if len(data) < 10:
        return ""

    with open(out, 'w') as f:
        f.write (data)

    return out

def gen_objdiff():
    data = '\n'
    for src_path_name, src_data in cfg.modules.items():
        src_path = getProjDir().joinpath(*str(src_path_name).split("/")).joinpath(*src_data.get("source_dir").split("/"))
        for src in sorted(src_path.rglob("**.*")):
            obj = file[1]
            name = file[1][len(str(getProjDir()))+1:].partition('.dir/')[2].rsplit(".", 1)[0]
            ctx = obj.rsplit('.', 1)[0] + '.ctx'
            #ctx = makeCtxFile(src, obj)
            data +=  "    {\n"
            data += f'      \"name\": "{name}",\n'
            data += f"      \"target_path\": \"{getElfPath()}\",\n"
            data += f"      \"base_path\": \"{obj}\",\n"
            data +=  "      \"scratch\": {\n"
            data +=  "        \"platform\": \"n3ds\",\n"
            data += f"        \"ctx_path\": \"{ctx}\",\n"
            data += f"        \"preset_id\": {cfg.preset_id},\n"
            data +=  "        \"build_ctx\": true\n"
            data +=  "      },\n"
            data +=  "      \"metadata\": {\n"
            data += f"        \"source_path\": \"{src}\",\n"
            data +=  "        \"auto_generated\": false\n"
            data +=  "      }\n"
            data +=  "    },\n"
            #print(Fore.LIGHTBLUE_EX + "objdiff.json: " + src + Fore.RESET + Style.RESET_ALL)
    data = data[:-2] + "\n"

    with open(Path(getProjDir()) / "data" / "template" / "objdiff.json", 'r') as template:
        with open(getJsonObjdiffFile(), 'w') as out:
            out.write(template.read().replace("$$$", data))

