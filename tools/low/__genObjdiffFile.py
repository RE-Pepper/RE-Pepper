#!/usr/bin/env python3
tools.low.glob import *
import json
import sys
from colorama import Fore, Style
tools.low.__genCtxFile import genCtx
from elftools.elf.elffile import ELFFile
from elftools.elf.sections import SymbolTableSection

def get_paths ():
    paths = []

    if not (Path(getBuildPath()) / "compile_commands.json").exists():
        raise FileNotFoundError (f"Cannot find compile_commands.json. Did you build?")
        return None

    with open(Path(getBuildPath()) / "compile_commands.json") as f:
        data = json.load(f)

    for e in data:
        paths.append((e.get("file"), Path(getBuildPath()) / e.get("output")))

    return paths

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

def genObjdiffJson():
    data = '\n'
    files = get_paths()
    for file in files:
        src = file[0]
        obj = file[1]
        name = file[1][len(getProjDir())+1:].partition('.dir/')[2].rsplit(".", 1)[0]
        ctx = obj.rsplit('.', 1)[0] + '.ctx'
        #ctx = makeCtxFile(src, obj)
        data +=  "    {\n"
        data += f'      \"name\": "{name}",\n'
        data += f"      \"target_path\": \"{getElfPath()}\",\n"
        data += f"      \"base_path\": \"{obj}\",\n"
        data +=  "      \"scratch\": {\n"
        data +=  "        \"platform\": \"n3ds\",\n"
        data += f"        \"ctx_path\": \"{ctx}\",\n"
        data += f"        \"preset_id\": {getPresetId()},\n"
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
        with open(Path(getProjDir()) / "objdiff.json", 'w') as out:
            out.write(template.read().replace("$$$", data))

def genObjdiffMakeRules():
    paths = get_paths()

    with open(Path(getBuildPath()) / "Makefile.ctx", 'w') as f:
        f.write("main:\n\t$(MAKE) --no-print-directory -f Makefile $(MAKECMDGOALS)\n\n")

        for src, obj in paths:
            ctx_path = obj.rsplit(".", 1)[0] + ".ctx"
            f.write(f"{ctx_path}:\n")
            f.write(f"\t@echo \"Generating {ctx_path} ...\"\n")
            f.write(f"\t@python ../tools/__genObjdiffFile.py {src}\n\n")

def genObjdiff():
    genObjdiffJson()
    genObjdiffMakeRules()
            
def main():
    if len(sys.argv) == 1:
        print ("Gen objdiff.json")
        genObjdiff()
        return

    file = sys.argv[1]

    src, obj = get_paths_for(file)
    if len(src) == 0 or len(obj) == 0:
        print (f"Cannot get {file} from compile_commands.json.")
        return

    ctx = makeCtxFile(src, obj)
    if len(ctx) == 0:
        print ("Context data is too short or empty.")
        return

    print(Fore.LIGHTBLUE_EX + "Made context: " + src + Fore.RESET + Style.RESET_ALL)

if __name__ == '__main__':
    main()
