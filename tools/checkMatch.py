#!/usr/bin/env python3
# Matching build verification.
#
# Compares the exported build code.bin against the original, byte for
# byte, attributes every difference to map rows, verifies that the
# pinned (rank O) regions of the linker map really sit at their
# original addresses, and reports anything that landed in the spill
# region behind the original image.
#
# Usage: python3 tools/checkMatch.py [-q] [-e] [-v]

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

def main():
    parser = argparse.ArgumentParser(description="Verify a matching build")
    parser.add_argument("-q", action="store_true", help="Quiet, only summary")
    parser.add_argument("-v", action="store_true", help="Verbose, list every bad row")
    parser.add_argument("-e", action="store_true", help="Exit with error code when not matching")
    parser.add_argument("--update", action="store_true", help="Demote pinned rows whose bytes differ into the match skip list, then exit")
    parser.add_argument("--skip", metavar="SYM", help="Demote a symbol (or ER_PIN_xxxxxxxx region name) by hand")
    args = parser.parse_args()

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

    orig_path = getBinCodeFile()
    build_path = getExportFile()

    if not orig_path.exists():
        fail_ex ("Original code.bin missing.", str(orig_path), False)
    if not build_path.exists():
        fail_ex ("Build code.bin missing.", str(build_path), False)

    header = read_header()
    text_lo = header[HeadType.Text][HeadVal.Start]
    rw_hi = header[HeadType.Rw][HeadVal.End]

    orig = orig_path.read_bytes()
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
    match_pct = 100.0 * (cmp_len - diff_bytes) / max(total, 1)

    echo ("")
    echo (f"Original: {len(orig)} bytes, Build: {len(build)} bytes")
    if len(build) < len(orig):
        echo (f"WARNING: build is {len(orig) - len(build)} bytes SHORTER than original")
    if len(build) > len(orig):
        echo (f"WARNING: build is {len(build) - len(orig)} bytes longer (spill content, see below)")
    echo (f"Matching bytes: {cmp_len - diff_bytes} / {total} ({match_pct:.4f}%)")
    echo ("")

    if diff_bytes == 0 and len(build) == len(orig):
        pass # the verdict line at the end says it
    else:
        echo (f"{len(diffs)} differing ranges, {diff_bytes} bytes total, {len(bad_rows)} rows affected:")
        shown = 0
        for idx, (name, first_addr, nbytes) in sorted(bad_rows.items(), key=lambda kv: kv[1][1]):
            if not args.v and shown >= MAX_REPORT:
                echo (f"  ... and {len(bad_rows) - shown} more (use -v to list all)")
                break
            r = rows[idx] if 0 <= idx < len(rows) else None
            extra = f" rank {r[MapFmt.Rank]} {r[MapFmt.Type]}" if r else ""
            echo (f"  {name} at 0x{first_addr:08X} ({nbytes} bytes){extra}")
            shown += 1
        echo ("")

    if pin_missing:
        echo (f"{len(pin_missing)} pinned region(s) missing or misplaced in the linker map:")
        for (addr, name), reg in pin_missing[:MAX_REPORT]:
            state = "absent" if reg is None else f"at 0x{reg['base']:08X}"
            echo (f"  {name} expected 0x{addr:08X}, region {state}")
        echo ("")

    if spill_sects:
        echo (f"Spill region holds {len(spill_sects)} section(s) beyond the original image:")
        for addr, size, sect, obj in spill_sects[:MAX_REPORT]:
            echo (f"  0x{addr:08X} 0x{size:X} {sect} ({obj})")
        if len(spill_sects) > MAX_REPORT:
            echo (f"  ... and {len(spill_sects) - MAX_REPORT} more")
        echo ("(dead weight in the .axf only, not in code.bin. usually losing")
        echo (" duplicate definitions next to original byte slices, or exidx)")

    ok = diff_bytes == 0 and len(build) == len(orig) and not pin_missing

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
            echo ("Rerun make.py --match, the output will be byte identical for these rows.")
        else:
            echo ("Nothing to demote: no differing byte range touches a pinned row.")
            if diff_bytes:
                echo ("(The differences sit in rows that were not pinned from compiled code.)")
        return

    if ok:
        echo ("MATCH: build code.bin is identical to the original.")
    else:
        echo ("NOT matching (see above).")
        echo ("Run with --update to demote differing pinned rows to original bytes.")

    if args.e and not ok:
        sys.exit(1)

if __name__ == "__main__":
    main()
