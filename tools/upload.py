#!/usr/bin/env python3
import sys
import os
import json
import cxxfilt
import requests
from elftools.elf.elffile import ELFFile
from elftools.elf.sections import SymbolTableSection
tools.low.__genCtxFile import genCtxs
tools.low.__parseMap import get_symbol
tools.low.glob import *

def find_source_path(str):
    with open(getElfPath(), "rb") as f:
        elf = ELFFile(f)
        last_file = None
        func_syms = []

        print ("Collecting functions ...")
        
        for section in elf.iter_sections():
            if not isinstance(section, SymbolTableSection):
                continue

            for sym in section.iter_symbols():
                if sym['st_info']['type'] == 'STT_FUNC':
                    func_syms.append (sym.name)


        print ("Finding file ...")
        
        for section in elf.iter_sections():
            if not isinstance(section, SymbolTableSection):
                continue

            for sym in section.iter_symbols():
                st_type = sym['st_info']['type']

                if st_type == 'STT_FILE':
                    last_file = sym.name

                elif st_type == 'STT_SECTION':
                    name = sym.name
                    if '.' not in name:
                        continue

                    _, after_dot = name.split('.', 1)

                    if after_dot not in func_syms:
                        continue

                    if str != after_dot:
                        continue

                    return last_file

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
        "preset": getPresetId ()
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
        print ("Missing argument: Symbol")
        return

    sym = sys.argv[1]
    path = find_source_path(sym)
    if (path is None):
        if(get_symbol(sym)):
            print ("Symbol found in map, but not in compilation. Make sure you put the symbol in a file before uploading!")
        else:
            print ("Symbol not found. Did you spell it correctly?")
        return

    print ("Collecting code ...")
    data, main = genCtxs(path, sym)

    #for line in data:
    #    print (line.rstrip('\n'))
    #for line in main:
    #    print (line.rstrip('\n'))

    path_obj = get_obj_path (path)
    if path_obj is None:
        print ("compile_commands.json missing, please build!")
        return

    name = cxxfilt.demangle (sym)

    print(f"Source file: {path}")
    print(f"Lines: ctx {len(data.splitlines())}, src {len(main.splitlines())}")
    if input("Ready to upload? (y/N): ").strip().lower() not in ("y", "yes", "j", "ja"):
        return
    
    base_url, claim_url = upload(sym, name, data, main, path_obj)

    print (f"Scratch created. Good luck matching {name}!.")
    print (f" -> Claim: {claim_url}")
    print (f" -> Url: {base_url}")

if __name__ == "__main__":
    main()

