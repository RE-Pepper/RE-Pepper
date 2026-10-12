#!/usr/bin/env python3
# 3differ watch mode: popup diff display that keeps itself up to date.
# watches every module source and the preinclude, reruns make.py when
# something changes and redraws the diff. ctrl+c leaves the final diff.
#
# usage: python3 tools/3differ/watch.py <version> <symbol|0xADDRESS> [--thumb]

import os
import sys
import time
import shutil
import argparse
import subprocess
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from tools.low.glob import *
from tools.low.utilsPrint import *
from tools.low.readSymMap import get_symbol, read_sym_file, MapFmt
from tools.low.readHeader import *

def snap_sources():
    # mtimes of every module source and the preinclude, os independent
    out = {}
    for mod_path_name, mod_data in cfg.modules.items():
        src_dir = mod_data.get("source_dir") or "."
        base = getProjDir().joinpath(*str(mod_path_name).split("/"))
        mod_src = base.joinpath(*str(src_dir).split("/"))
        if not mod_src.is_dir():
            continue
        for f in mod_src.rglob("*"):
            if f.is_file():
                try:
                    out[str(f)] = f.stat().st_mtime
                except OSError:
                    pass
    if cfg.flag_preinclude:
        p = getProjDir() / cfg.flag_preinclude
        if p.exists():
            out[str(p)] = p.stat().st_mtime
    return out

def build():
    r = subprocess.run(
        [sys.executable, str(getProjDir() / "make.py"), getVersion()],
        capture_output=True, text=True,
    )
    return r.returncode == 0, (r.stdout or "") + (r.stderr or "")

def render(sym, thumb_hint, full, err):
    import importlib
    differ = importlib.import_module("tools.3differ")

    w, _ = shutil.get_terminal_size((100, 40))
    print("\033[2J\033[H", end="")
    echo (f"{cfg.project_name} v{getVersion().upper()}  {sym[MapFmt.Symbol] or hex(sym[MapFmt.Start])}")
    print("─" * min(w, 100))
    if err:
        print("\033[31m" + "build failed:" + "\033[0m")
        for l in err.splitlines()[-12:]:
            print("  " + l)
        return None
    res = differ.diff_symbol(sym, thumb_hint=thumb_hint, color=True, full=full)
    print(res.stdout)
    return res

def main():
    parser = argparse.ArgumentParser(description="3differ watch mode")
    parser.add_argument("version", help="Version")
    parser.add_argument("symbol", help="Map symbol or 0xADDRESS")
    parser.add_argument("--thumb", action="store_true", help="Force thumb")
    parser.add_argument("--full", action="store_true", help="Show whole function")
    args = parser.parse_args()

    setVersion(args.version)

    sym = None
    if args.symbol.startswith("0x"):
        addr = int(args.symbol, 0)
        for r in read_sym_file():
            if r[MapFmt.Start] == addr:
                sym = r
                break
    else:
        sym = get_symbol(args.symbol)
    if sym is None:
        fail_ex ("Symbol not found in map.", args.symbol, False)

    thumb_hint = True if args.thumb else None
    err = None
    res = None

    try:
        ok, err = build()
        res = render(sym, thumb_hint, args.full, err if not ok else None)
        sources = snap_sources()
        while True:
            time.sleep(1.0)
            now = snap_sources()
            if now != sources:
                sources = now
                ok, err = build()
                res = render(sym, thumb_hint, args.full, err if not ok else None)
    except KeyboardInterrupt:
        pass

    # leaving the last state visible
    if res is not None:
        echo ("final state:")
        print (res.stdout)

if __name__ == "__main__":
    main()
