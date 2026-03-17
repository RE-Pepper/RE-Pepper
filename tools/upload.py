#!/usr/bin/env python3
import sys
import os
import json
import struct
import requests
from capstone import *
from capstone.arm import *

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from tools.low.genContext import gen_ctx
from tools.low.getSymFile import get_sym_file
from tools.low.readSymMap import *
from tools.low.readHeader import *
from tools.low.glob import *
from tools.pypstem.manSetup import setup_compiler
from tools.pypstem._utils import getFileBuildPath

try:
    import cxxfilt
    is_filter = True
except ImportError:
    echo ("cxxfilt module not found, not demangling.")
    is_filter = False

def get_asm (sym_name):
    lines = []
    sym = get_symbol(sym_name)
    if not sym:
        fail (f"get_asm cannot find sym for {sym_name}")

    # read offsets
    base_addr = read_header()[HeadType.Text][HeadVal.Start]
    addr_start = sym[MapFmt.Start] - base_addr
    addr_end_code = sym[MapFmt.Pool] - base_addr
    addr_end_func = sym[MapFmt.End] - base_addr

    # read binary
    with open(getBinFile(), 'rb') as f:
        data = f.read()
    data_view = memoryview(data)

    # init capstone
    md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
    md.detail = True

    instrs = list(md.disasm(data_view[addr_start:addr_end_code], 0))

    for i in instrs:
        mnem = i.mnemonic
        str = i.op_str
        if mnem.startswith("b") and str.startswith("#"):
            str = str.replace("#", "")
        lines.append(f"    {mnem}\t\t{str}")

    if addr_end_func > addr_end_code:
        for data in range(addr_end_code, addr_end_func, 4):
            val = struct.unpack_from("<I", data_view, data)[0]
            lines.append(f"    .word\t0x{val:08X}")

    return "\n".join(lines)

def upload (sym_name, show_name, ctx, src):
    echo ("Uploading ...")

    url = f"https://decomp.me/api/scratch"
    asm = get_asm(sym_name)

    if not ctx and not src:
        data = {
            "name": show_name,
            "context": "",
            "target_asm": asm,
            "diff_label": sym_name,
            "preset": cfg.decompme_id
        }
    else:
        data = {
            "name": show_name,
            "context": ctx,
            "source_code": src,
            "target_asm": asm,
            "diff_label": sym_name,
            "preset": cfg.decompme_id
        }

    r = requests.post(url, data=data)

    if not r.ok:
        fail (f"{r.status_code} - {r.text}")

    res = r.json()

    slug = res.get("slug")
    claim_token = res.get("claim_token")

    if not slug or not claim_token:
        fail (f"Unexpected response: {res}")
    
    base_url = f"{api_base}/scratch/{slug}/"
    claim_url = f"{api_base}/scratch/{slug}/claim?token={claim_token}"

    return base_url, claim_url

def main():
    if len(sys.argv) <= 1:
        fail ("Missing argument: Symbol", False)

    sym_in = sys.argv[1]
    path, sym = get_sym_file(sym_in)

    if not path:
        data = None
        main = None
    else:
        echo ("Collecting code ...")
        data, main = gen_ctx(path, sym)

    if is_filter:
        name = cxxfilt.demangle (sym)
    else:
        name = sym

    if path:
        echo (f"Lines: ctx {len(data.splitlines())}, src {len(main.splitlines())}")
    else:
        echo ("No file found, ctx will be empty.")

    if input("Ready to upload? (y/N) ").strip().lower() not in ("y", "yes", "j", "ja"):
        return

    base_url, claim_url = upload(sym, name, data, main)

    echo (f"Scratch created. Good luck matching {name}, and may armcc be with you.")
    echo (f" -> Claim: {claim_url}")
    echo (f" -> Url: {base_url}")

if __name__ == "__main__":
    main()

