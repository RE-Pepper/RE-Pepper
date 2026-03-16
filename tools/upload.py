#!/usr/bin/env python3
import sys
import os
import json
import requests
from elftools.elf.elffile import ELFFile
from elftools.elf.sections import SymbolTableSection

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from tools.low.genContext import gen_ctx, find_file_path
from tools.low.readSymMap import get_symbol
from tools.low.glob import *

try:
    import cxxfilt
    is_filter = True
except ImportError:
    echo ("cxxfilt module not found, not demangling.")
    is_filter = False

def find_source_path(sym_name):
    with open(getElfFile(), "rb") as f:
        elf = ELFFile(f)

        for section in elf.iter_sections():
            if not isinstance(section, SymbolTableSection):
                continue

            # found sym section
            last_file = None

            for sym in section.iter_symbols():
                sym_type = sym['st_info']['type']

                if (sym.name.startswith("$")):
                    continue

                echo (sym.name)
                #if (sym_type == "STT_FILE"):
                #    last_file = sym.name
                #elif not (last_file == str(getDependFile())):
                #    if sym_name == sym.name:
                #        echo (sym.name)
                #        return str(last_file)

            break

    return None

def get_obj_path (str):
    if not os.path.exists(Path(getBuildPath()) / "compile_commands.json"):
        return None

    with open(Path(getBuildPath()) / "compile_commands.json") as f:
        data = json.load(f)

    for e in data:
        if e.get("file") == (str):
            return f'{getBuildPath()}/{e.get("output")}'

def upload (sym_name, show_name, ctx, src, obj_path):
    print ("Uploading ...")

    api_base = "https://decomp.me"
    url = f"{api_base}/api/scratch"
    
    files = {
        "target_obj": open (obj_path, 'rb')
    }
    data = {
        "name": show_name,
        "context": ctx,
        "source_code": src,
        "diff_label": sym_name,
        "preset": cfg.preset_id
    }

    r = requests.post(url, files=files, data=data)

    if not r.ok:
        print("Error:", r.status_code, r.text)
        return None, None

    res = r.json()

    slug = res.get("slug")
    claim_token = res.get("claim_token")

    if not slug or not claim_token:
        print("Unexpected response:", res)
        return None, None
    
    base_url = f"{api_base}/scratch/{slug}/"
    claim_url = f"{api_base}/scratch/{slug}/claim?token={claim_token}"

    return base_url, claim_url

def main():
    if len(sys.argv) <= 1:
        fail ("Missing argument: Symbol", False)


    echo ("Finding source file ...")

    sym = sys.argv[1]
    path = find_source_path(sym)
    if not path:
        if(get_symbol(sym)):
            fail ("Symbol found in map, but not in compilation. Make sure you put the symbol in a file before uploading!")
        else:
            fail ("Symbol not found. Did you spell it correctly?")

    echo (f"Found in {path}")

    echo ("Collecting code ...")
    data, main = genCtxs(path, sym)

    #for line in data:
    #    print (line.rstrip('\n'))
    #for line in main:
    #    print (line.rstrip('\n'))

    path_obj = get_obj_path (path)
    if path_obj is None:
        fail ("compile_commands.json missing, please build!")

    if is_filter:
        name = cxxfilt.demangle (sym)
    else:
        name = sym

    echo (f"Source file: {path}")
    echo (f"Lines: ctx {len(data.splitlines())}, src {len(main.splitlines())}")
    if input("Ready to upload? (y/N) ").strip().low.r() not in ("y", "yes", "j", "ja"):
        return

    base_url, claim_url = upload(sym, name, data, main, path_obj)

    echo (f"Scratch created. Good luck matching {name}, and may armcc be with you.")
    echo (f" -> Claim: {claim_url}")
    echo (f" -> Url: {base_url}")

if __name__ == "__main__":
    main()

