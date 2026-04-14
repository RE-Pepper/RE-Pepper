#!/usr/bin/env python3

from tools.low.glob import *

def is_sym_map_diff():
    if not getMapFile().exists():
        fail ("Version not configured, cannot split.")

    ts_new = int(getMapFile().stat().st_mtime)

    def write_new():
        with open(getCfgMapFile(), "w") as f:
            f.write(f"{getVersion()} {ts_new}")

    if not getCfgMapFile().exists():
        write_new()
        return True

    ts_old = 0
    ver_old = 0
    with open(getCfgMapFile(), "r") as f:
        ver_old, ts_old = next(f).split()

    if getVersion() != ver_old:
        write_new()
        return True
    if int(ts_old) != ts_new:
        write_new()
        return True

    return False
