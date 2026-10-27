#!/usr/bin/env python3
# byte checker behind tools/diff.py --match. builds the
# decompiled / incbin split from the unit
# decomposition, byte compares the exported code.bin against the
# original and prints the verdict. differences attribute to map rows,
# missing pins and spill content only show when something is wrong.
# usage: python3 tools/diff.py --match -q -e -v --update [--skip SYM]

import sys
import time
import argparse
from bisect import bisect_right
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from tools.low.glob import *
from tools.low.readSymMap import *
from tools.low.readHeader import *
from tools.low.utilsPrint import *

MAX_REPORT = 32

def read_skip_list():
    syms = set()
    f = getMatchSkipFile()
    if f.exists():
        for line in f.read_text().splitlines():
            line = line.split("#")[0].strip()
            if line:
                syms.add(line)
    return syms

def write_skip_list(syms):
    f = getMatchSkipFile()
    existing = read_skip_list()
    with open(f, "a") as fh:
        for name in syms:
            if name not in existing:
                fh.write(name + "\n")
                existing.add(name)

def resolve_pin_names():
    # the same decomposition the generator builds: only the head row of
    # a pin unit is a pin, absorbed rows inside a block are not
    from tools.low.genOriginal import build_units
    units, _header = build_units()
    return {u.start: u.rows[0][MapFmt.Symbol] for u in units if u.kind in ("pin", "zpin")}

def decomp_stats():
    # pin bytes per module (from .syms) plus the incbin rest
    import json
    from tools.low.genOriginal import build_units
    units, _header = build_units()

    mods = {}
    if getCfgSymsFile().exists():
        with open(getCfgSymsFile()) as f:
            syms_files = json.load(f)
        sym_mod = {}
        for src, syms in syms_files.items():
            best = None
            for mod_path_name, mod_data in cfg.modules.items():
                mod_subdir = mod_data.get("source_dir") or "."
                mod = mod_path_name if mod_subdir in (".", "", None) else f"{mod_path_name}/{mod_subdir}"
                if str(src).startswith(mod) and len(mod) > len(best or ""):
                    best = mod_data.get("name") or mod_path_name
            for s in syms:
                sym_mod[s] = best or "Unknown"

        for u in units:
            if u.kind not in ("pin", "zpin"):
                continue
            cat = sym_mod.get(u.rows[0][MapFmt.Symbol], "Unknown")
            mods.setdefault(cat, 0)
            mods[cat] += u.end - u.start

    pinned_total = sum(mods.values())
    total = max(sum(u.end - u.start for u in units), 1)
    return mods, pinned_total, total

# ---------------------------------------------------------------------------
# linker map parsing

def parse_linker_map():
    # -> (regions, symbols)
    # regions: {name: {"base": int, "size": int, "sections": [(addr,size,sect,obj)]}}
    # symbols: {name: (addr, size)}
    path = getOutMapFile()
    if not path.exists():
        warn(f"Linker map not found ({path}), skipping map based checks.")
        return {}, {}

    regions = {}
    symbols = {}
    cur = None
    in_syms = False

    with open(path, "r", errors="replace") as f:
        for line in f:
            line = line.rstrip()

            if "Execution Region " in line and " (Base:" in line:
                try:
                    name = line.split("Execution Region ")[1].split(" ")[0]
                    base = int(line.split("Base: ")[1].split(",")[0], 16)
                    size = int(line.split("Size: ")[1].split(",")[0], 16)
                except (IndexError, ValueError):
                    cur = None
                    continue
                cur = {"base": base, "size": size, "sections": []}
                regions[name] = cur
                in_syms = False
                continue

            if "Global Symbols" in line:
                in_syms = True
                cur = None
                continue
            if line.startswith("===") and in_syms:
                in_syms = False
                continue

            if in_syms:
                parts = [p for p in line.split() if p != "ABSOLUTE"]
                if len(parts) < 4 or not parts[1].startswith("0x"):
                    continue
                try:
                    symbols[parts[0]] = (int(parts[1], 16), int(parts[3], 0))
                except ValueError:
                    continue
                continue

            if cur is not None:
                sline = line.strip()
                if sline.startswith("0x") and not sline.endswith("Object"):
                    parts = sline.split()
                    if len(parts) < 6:
                        continue
                    try:
                        addr = int(parts[0], 16)
                        size = int(parts[1], 16)
                    except ValueError:
                        continue
                    sect = parts[5]
                    obj = " ".join(parts[6:]) if len(parts) > 6 else "?"
                    cur["sections"].append((addr, size, sect, obj))

    return regions, symbols

# ---------------------------------------------------------------------------

def main(argv=None):
    parser = argparse.ArgumentParser(description="Verify a matching build")
    parser.add_argument("-q", action="store_true", help="Quiet, only summary")
    parser.add_argument("-v", action="store_true", help="Verbose, list every bad row")
    parser.add_argument("-e", action="store_true", help="Exit with error code when not matching")
    parser.add_argument("--update", action="store_true", help="Demote pinned rows whose bytes differ into the match skip list, then exit")
    parser.add_argument("--skip", metavar="SYM", help="Demote a symbol (or ER_PIN_xxxxxxxx region name) by hand")
    args = parser.parse_args(argv)

    # honor the version make.py last selected (data/.version), the map
    # only parses lazily so this is safe after the imports above
    from tools.low.utilsVersion import get_ver
    setVersion(get_ver())

    # ---- manual demote
    if args.skip:
        target = args.skip
        if target.upper().startswith("ER_PIN_"):
            addr = int(target.split("_")[-1], 16)
            hit = next((r for r in read_sym_file() if r[MapFmt.Start] == addr and r[MapFmt.Symbol]), None)
            if not hit:
                fail_ex ("No map row at that address.", target, False)
            target = hit[MapFmt.Symbol]
        write_skip_list([target])
        echo (f"Demoted to original bytes: {target}")
        echo ("Rerun make.py --match to apply.")
        return

    orig_path = getBinFile()
    build_path = getExportFile()

    if not orig_path.exists():
        fail_ex ("Original code.bin or game.axf missing.", str(orig_path), False)
    if not build_path.exists():
        fail_ex ("Build code.bin missing.", str(build_path), False)

    header = read_header()
    text_lo = header[HeadType.Text][HeadVal.Start]
    rw_hi = header[HeadType.Rw][HeadVal.End]

    orig = readBinImage()
    build = build_path.read_bytes()

    rows = sorted(read_sym_file(), key=lambda r: r[MapFmt.Start])
    starts = [r[MapFmt.Start] for r in rows]

    # ---- byte comparison
    cmp_len = min(len(orig), len(build))
    diffs = []
    i = 0
    while i < cmp_len:
        if orig[i] != build[i]:
            j = i
            while j < cmp_len and orig[j] != build[j]:
                j += 1
            diffs.append((i, j))
            i = j
        else:
            i += 1

    diff_bytes = sum(b - a for a, b in diffs)

    # ---- attribute diffs to rows
    bad_rows = {}
    for a, b in diffs:
        addr = text_lo + a
        idx = bisect_right(starts, addr) - 1
        if idx < 0:
            row_name = f"<before {text_lo:08X}>"
        else:
            r = rows[idx]
            row_name = r[MapFmt.Symbol] or (f"fn_{r[MapFmt.Start]:08X}" if "f" in r[MapFmt.Type] else f"dat_{r[MapFmt.Start]:08X}")
        entry = bad_rows.setdefault(idx, [row_name, text_lo + a, 0])
        entry[2] += b - a

    # ---- pinned regions in the linker map
    have_map = getOutMapFile().exists()
    regions, symbols = parse_linker_map()
    # the same pin candidate set the generator uses (respects
    # only_matching and the match skip list)
    candidates = resolve_pin_names()
    pinned = [(addr, name) for addr, name in sorted(candidates.items())]
    pin_missing = []
    if have_map:
        for addr, name in pinned:
            reg = regions.get(f"ER_PIN_{addr:08X}")
            if reg is None or reg["base"] != addr or not reg["sections"]:
                pin_missing.append(((addr, name), reg))

    # ---- spill
    spill = regions.get("ER_SPILL")
    spill_sects = spill["sections"] if spill else []

    # ---- report
    total = len(orig)
    mods, pin_bytes, unit_bytes = decomp_stats()
    decomp_pct = 100.0 * pin_bytes / unit_bytes
    incbin_pct = 100.0 - decomp_pct

    ok = diff_bytes == 0 and len(build) == len(orig) and not pin_missing

    echo ("")
    for cat in sorted(mods):
        pct = 100.0 * mods[cat] / unit_bytes
        echo (f"{cat:10s} - {pct:6.2f}%  ({mods[cat]} bytes)")
    echo ("")
    echo (f"decompiled {decomp_pct:.2f}% ({pin_bytes} bytes) | incbin {incbin_pct:.2f}%")

    if ok:
        echo ("MATCH: code.bin is identical to the original.")
    else:
        echo ("")
        if len(build) != len(orig):
            if len(build) < len(orig):
                echo (f"WARNING: build is {len(orig) - len(build)} bytes SHORTER than original")
            else:
                echo (f"WARNING: build is {len(build) - len(orig)} bytes longer (spill, see below)")
        echo (f"MISMATCH: {len(diffs)} differing ranges, {diff_bytes} bytes, {len(bad_rows)} rows:")
        shown = 0
        for idx, (name, first_addr, nbytes) in sorted(bad_rows.items(), key=lambda kv: kv[1][1]):
            if not args.v and shown >= MAX_REPORT:
                echo (f"  ... and {len(bad_rows) - shown} more (use -v to list all)")
                break
            r = rows[idx] if 0 <= idx < len(rows) else None
            extra = f" rank {r[MapFmt.Rank]} {r[MapFmt.Type]}" if r else ""
            echo (f"  {name} at 0x{first_addr:08X} ({nbytes} bytes){extra}")
            shown += 1
        if pin_missing:
            echo (f"{len(pin_missing)} pinned region(s) missing or misplaced in the linker map:")
            for (addr, name), reg in pin_missing[:MAX_REPORT]:
                state = "absent" if reg is None else f"at 0x{reg['base']:08X}"
                echo (f"  {name} expected 0x{addr:08X}, region {state}")
        if spill_sects:
            echo (f"spill region holds {len(spill_sects)} section(s) beyond the original image:")
            for addr, size, sect, obj in spill_sects[:MAX_REPORT]:
                echo (f"  0x{addr:08X} 0x{size:X} {sect} ({obj})")
            if len(spill_sects) > MAX_REPORT:
                echo (f"  ... and {len(spill_sects) - MAX_REPORT} more")
            echo ("(dead weight in the .axf only, not in code.bin)")
        echo ("")
        echo ("Run with --update to demote differing pinned rows to original bytes.")

    # ---- auto demote
    if args.update:
        candidates = resolve_pin_names()
        to_demote = []
        for a, b in diffs:
            lo_a, hi_b = text_lo + a, text_lo + b
            for r in rows:
                if r[MapFmt.Start] not in candidates:
                    continue
                end = r[MapFmt.End] or r[MapFmt.Start]
                if r[MapFmt.Start] < hi_b and end > lo_a:
                    name = candidates[r[MapFmt.Start]]
                    if name not in to_demote:
                        to_demote.append(name)
        if to_demote:
            for name in to_demote:
                echo (f"Demoted to original bytes: {name}")
            write_skip_list(to_demote)
            echo (f"{len(to_demote)} pinned row(s) demoted into {getMatchSkipFile()}.")
            echo ("Rerun make.py, the output will be byte identical for these rows.")
        else:
            echo ("Nothing to demote: no differing byte range touches a pinned row.")
        return

    if args.e and not ok:
        sys.exit(1)

if __name__ == "__main__":
    main()
