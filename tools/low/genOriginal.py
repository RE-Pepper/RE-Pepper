#!/usr/bin/env python3
# matching mode: original byte filler generator.
# file ranges become units, shared with gen_scatter_match:
#   pin    map row with a compiled section, placed at its address
#   slice  run of original code.bin bytes (INCBIN), named rows get a label
# a row with a SectionName spanning the rows at its start is a per file
# data block and absorbs them.

import re
import shutil

from tools.low.glob import *
from tools.low.readSymMap import *
from tools.low.readHeader import *
from tools.low.getSection import typeToSectionLinker
from tools.low.utilsPrint import *

ORIG_AREAS_PER_FILE = 100
# armasm does not cope with one giant source: .s files rotate after
# this many label points
ORIG_LABELS_MAX = 240
ORIG_LABELS_PER_FILE = 256

RE_SPECIAL = re.compile(r'[^a-zA-Z0-9_]')
# armasm built in names, cannot be defined even pipe quoted (A1108E)
ARMASM_BUILTIN = re.compile(r'^(?:r|a|v|c|p|w|s|d|q)\d+$|^(?:sb|sl|fp|ip|sp|lr|pc)$', re.IGNORECASE)

def asm_sym(name):
    # pipe quote always: plain labels would collide with built in names,
    # the object symbol keeps the plain name
    return f"|{name}|"

def orig_unit_label(start):
    return f"origunit_{start:08X}"

def orig_area_name(start):
    return f".orig.{start:08X}"

# ---------------------------------------------------------------------------
# pin decision inputs

_known_syms = None
_skip_syms = None

def _load_json_set(path, what):
    syms = set()
    if path.exists():
        import json
        try:
            with open(path, "r") as f:
                data = json.load(f)
            for syms_list in data.values():
                syms.update(syms_list)
        except Exception as e:
            warn(f"Cannot read {what} ({path}): {e}")
    return syms

def _load_known_syms():
    # symbols that exist in built objects (.syms is written by exec_build)
    global _known_syms
    if _known_syms is None:
        _known_syms = _load_json_set(getCfgSymsFile(), ".syms build cache")
    return _known_syms

def _load_skip_syms():
    global _skip_syms
    if _skip_syms is None:
        _skip_syms = set()
        f = getMatchSkipFile()
        if f.exists():
            for line in f.read_text().splitlines():
                line = line.split("#")[0].strip()
                if line:
                    _skip_syms.add(line)
    return _skip_syms

# ---------------------------------------------------------------------------
# unit decomposition

class Unit:
    __slots__ = ("kind", "start", "end", "rows", "code", "rw")
    # kind: "pin"/"slice" for text/ro/rw, "zpin"/"zslice" for bss
    # code: text segment slice (CODE area)
    # rw:   rw segment slice (READWRITE area)
    def __init__(self, kind, start, end, rows, code, rw=False):
        self.kind = kind
        self.start = start
        self.end = end
        self.rows = rows
        self.code = code
        self.rw = rw

_aliases = set()

def is_pinnable(row, zero_init, span_block=False):
    name = row[MapFmt.Symbol]
    if not name:
        return False
    is_bss = "b" in row[MapFmt.Type]
    if is_bss != zero_init:
        return False
    if row[MapFmt.End] is None or row[MapFmt.End] <= row[MapFmt.Start]:
        return False
    if row[MapFmt.Start] % 4 or row[MapFmt.End] % 4:
        return False # fixed region bases and content must be word aligned
    if row[MapFmt.Start] in _aliases and not span_block:
        return False # several rows share this start, keep the bytes whole
    if name in _load_skip_syms():
        return False # known non matching, use original bytes
    if cfg.only_matching and row[MapFmt.Rank] != "O":
        return False # strict mode: only verified matching rows
    if name not in _load_known_syms():
        return False # no compiled version available, use original bytes
    return True

def _block_candidate(group):
    # a per file data block spans all rows at its start, wins over the
    # alias protection
    if len(group) < 2:
        return group[0], False
    named = [r for r in group if r[MapFmt.SectionName]]
    if len(named) == 1:
        cand = named[0]
        if cand[MapFmt.End] is not None and all(r[MapFmt.End] is None or r[MapFmt.End] <= cand[MapFmt.End] for r in group):
            return cand, True
    return group[0], False

def _flush_slice(units, a, b, labels, zero_init, code, rw=False):
    if b > a:
        units.append(Unit("zslice" if zero_init else "slice", a, b, labels, code, rw))

def _walk_segment(units, grouped, lo, hi, zero_init, code, rw=False):
    cursor = lo
    labels = []

    for start, group in grouped:
        if start >= hi:
            break
        if start < cursor:
            # row inside a pinned block, the compiled section carries it
            continue
        row, span_block = _block_candidate(group)
        if is_pinnable(row, zero_init, span_block):
            # close the open slice right before the pinned row
            _flush_slice(units, cursor, row[MapFmt.Start], labels, zero_init, code, rw)
            units.append(Unit("zpin" if zero_init else "pin",
                              row[MapFmt.Start], row[MapFmt.End], group, code, rw))
            cursor = row[MapFmt.End]
            labels = []
        else:
            for r in group:
                name = r[MapFmt.Symbol]
                if not name:
                    continue
                if ARMASM_BUILTIN.match(name):
                    warn(f"{name} at 0x{start:08X} collides with an armasm register name, no slice label (pin it or it cannot be referenced)")
                    continue
                labels.append(r)

    _flush_slice(units, cursor, hi, labels, zero_init, code, rw)

def _split_units(units):
    # split long slices at word aligned label starts, one AREA per part
    out = []
    for u in units:
        if u.kind not in ("slice", "zslice") or len(u.rows) <= ORIG_LABELS_MAX:
            out.append(u)
            continue

        parts = []
        cur_rows = []
        cur_start = u.start
        prev_rs = None
        for r in u.rows:
            rs = r[MapFmt.Start]
            if cur_rows and rs % 4 == 0 and rs != prev_rs and len(cur_rows) >= ORIG_LABELS_MAX:
                parts.append(Unit(u.kind, cur_start, rs, cur_rows, u.code, u.rw))
                cur_start = rs
                cur_rows = []
            cur_rows.append(r)
            prev_rs = rs
        parts.append(Unit(u.kind, cur_start, u.end, cur_rows, u.code, u.rw))

        if len(parts) > 1:
            out.extend(parts)
        else:
            out.append(u)
    return out

def build_units():
    # returns (units, header), units ascending over [text_start, rw_end),
    # plus bss units when the map has bss rows. the bytes after rw_end
    # are makerom page padding and are handled at export.
    global _aliases

    header = read_header()
    text_lo = header[HeadType.Text][HeadVal.Start]
    text_hi = header[HeadType.Text][HeadVal.End]
    ro_lo   = header[HeadType.Ro][HeadVal.Start]
    ro_hi   = header[HeadType.Ro][HeadVal.End]
    rw_lo   = header[HeadType.Rw][HeadVal.Start]
    rw_hi   = header[HeadType.Rw][HeadVal.End]
    bss_lo  = header[HeadType.Bss][HeadVal.Start]
    bss_hi  = header[HeadType.Bss][HeadVal.End]

    code_path = getBinCodeFile()
    if not code_path.exists():
        fail_ex ("Matching mode needs the original code.bin.", f"Missing: {code_path}", False)
    bin_end = text_lo + code_path.stat().st_size

    if not (text_lo <= text_hi <= ro_lo <= ro_hi <= rw_lo <= rw_hi):
        fail_ex ("Header sections out of order.", f"TEXT 0x{text_lo:X}-0x{text_hi:X}, RO 0x{ro_lo:X}-0x{ro_hi:X}, RW 0x{rw_lo:X}-0x{rw_hi:X}", False)
    if bss_lo != rw_hi:
        warn(f"BSS start 0x{bss_lo:X} does not touch RW end 0x{rw_hi:X}")

    syms = sorted(read_sym_file(), key=lambda s: s[MapFmt.Start])

    # group rows by start address (rows can alias the same range)
    grouped = {}
    for s in syms:
        grouped.setdefault(s[MapFmt.Start], []).append(s)
    _aliases = {a for a, g in grouped.items() if len(g) > 1}
    grouped = sorted(grouped.items())

    for s, g in grouped:
        if rw_hi <= s < bin_end:
            warn(f"Row {g[0][MapFmt.Symbol] or '?'} at 0x{s:08X} lies in the RW page padding, skipped")
        if s >= bss_hi:
            warn(f"Row {g[0][MapFmt.Symbol] or '?'} at 0x{s:08X} lies beyond BSS end, skipped")

    units = []

    # file backed ranges
    _walk_segment(units, [(s, g) for s, g in grouped if text_lo <= s < text_hi], text_lo, text_hi, False, True)
    _flush_slice(units, text_hi, ro_lo, [], False, True)   # text -> ro pad
    _walk_segment(units, [(s, g) for s, g in grouped if ro_lo <= s < ro_hi], ro_lo, ro_hi, False, False)
    _flush_slice(units, ro_hi, rw_lo, [], False, False)    # ro -> rw pad
    _walk_segment(units, [(s, g) for s, g in grouped if rw_lo <= s < rw_hi], rw_lo, rw_hi, False, False, rw=True)

    # zero init range (bss), if the map has rows there
    bss_rows = [(s, g) for s, g in grouped if bss_lo <= s < bss_hi]
    if bss_rows:
        _walk_segment(units, bss_rows, bss_lo, bss_hi, True, False)

    units = _split_units(units)


    last = text_lo
    for u in units:
        if u.kind.startswith("z"):
            continue
        if u.end < u.start or u.start < text_lo:
            fail_ex ("Unit decomposition failed.", f"Bad unit 0x{u.start:X}-0x{u.end:X} ({u.kind})", False)
        if u.start < last:
            fail_ex ("Unit decomposition failed: overlap.", f"Unit 0x{u.start:X} starts before 0x{last:X}", False)
        if u.start > last:
            fail_ex ("Unit decomposition failed: hole.", f"Range 0x{last:X}-0x{u.start:X} not covered", False)
        last = u.end
    if last != rw_hi:
        fail_ex ("Unit decomposition failed: coverage.", f"Units end at 0x{last:X}, RW ends at 0x{rw_hi:X}", False)

    return units, header

# ---------------------------------------------------------------------------
# slice emission

def _slice_chunks(unit):
    # one chunk per label point, armasm INCBIN has no offset support.
    # yields (offset, [rows], chunk_len)
    offs = {}
    total = unit.end - unit.start
    for r in unit.rows:
        off = r[MapFmt.Start] - unit.start
        if off < 0 or off >= total:
            warn(f"Row {r[MapFmt.Symbol]} outside slice 0x{unit.start:08X}, skipped")
            continue
        offs.setdefault(off, []).append(r)

    keys = sorted(offs)
    chunks = []
    cur = 0
    for i, off in enumerate(keys):
        if off > cur:
            chunks.append((cur, [], off - cur))
        end = keys[i + 1] if i + 1 < len(keys) else total
        chunks.append((off, offs[off], end - off))
        cur = end
    if cur < total:
        chunks.append((cur, [], total - cur))
    return chunks

def _emit_slice_asm(f, unit, bin_data, text_lo):
    area = orig_area_name(unit.start)
    if unit.kind == "zslice":
        f.write(f"    AREA |{area}|,NOINIT,READWRITE,ALIGN=2\n")
    elif unit.code:
        f.write(f"    AREA |{area}|,CODE,READONLY,ALIGN=2\n")
    elif unit.rw:
        f.write(f"    AREA |{area}|,DATA,READWRITE,ALIGN=2\n")
    else:
        f.write(f"    AREA |{area}|,DATA,READONLY,ALIGN=2\n")

    # keep alive label: depend.o imports it so the area survives --remove
    f.write(f"    EXPORT {orig_unit_label(unit.start)}\n")
    f.write(f"{orig_unit_label(unit.start)}\n")

    for off, labels, size in _slice_chunks(unit):
        if size <= 0:
            continue
        opened_func = False
        for r in labels:
            f.write(f"    EXPORT {asm_sym(r[MapFmt.Symbol])}\n")
        for r in labels:
            f.write(f"{asm_sym(r[MapFmt.Symbol])}")
            if unit.code and "f" in r[MapFmt.Type] and not opened_func:
                # one FUNCTION marker per chunk, ENDFUNC closes it below
                f.write(" FUNCTION")
                opened_func = True
            f.write("\n")
        if unit.kind == "slice":
            addr = unit.start + off
            data = bin_data[addr - text_lo : addr - text_lo + size]
            name = f"{addr:08X}.bin"
            # armasm resolves a bare INCBIN name against the source
            # file directory, the only reliable form under wibo
            with open(getOrigAsmDir() / name, "wb") as bf:
                bf.write(data)
            f.write(f"    INCBIN {name}\n")
        else:
            f.write(f"    SPACE {size}\n")
        if opened_func:
            f.write("    ENDFUNC\n")

def _gen_stamp():
    # .syms is rewritten every build, stamp it by content not mtime
    import hashlib
    parts = [getVersion()]
    parts.append(str(int(getMapFile().stat().st_mtime)) if getMapFile().exists() else "0")
    syms = getCfgSymsFile()
    if syms.exists():
        parts.append(hashlib.sha1(syms.read_bytes()).hexdigest())
    else:
        parts.append("none")
    for p in (getBinCodeFile(), getMatchSkipFile()):
        parts.append(str(int(p.stat().st_mtime)) if p.exists() else "0")
    return " ".join(parts)

def gen_original(clear=False):
    # generate the original byte slices.
    # returns True when outputs were regenerated
    stamp_f = getOrigDir() / ".stamp"
    stamp = _gen_stamp()

    if not clear and stamp_f.exists() and stamp_f.read_text().strip() == stamp and getOrigAsmDir().exists():
        asm = list(getOrigAsmDir().glob("*.s"))
        obj = list(getOrigObjDir().glob("*.o")) if getOrigObjDir().exists() else []
        if asm and len(asm) == len(obj):
            return False

    echo ("Generating original byte slices")
    units, header = build_units()
    text_lo = header[HeadType.Text][HeadVal.Start]

    with open(getBinCodeFile(), "rb") as f:
        bin_data = f.read()

    if getOrigDir().exists():
        shutil.rmtree(getOrigDir(), ignore_errors=True)
    getOrigAsmDir().mkdir(parents=True, exist_ok=True)

    slices = [u for u in units if u.kind in ("slice", "zslice")]
    pins   = [u for u in units if u.kind in ("pin", "zpin")]

    file_i = 0
    area_count = 0
    label_count = 0
    f = open(getOrigAsmDir() / f"orig_{file_i:02d}.s", "w")
    f.write("; AUTOGENERATED original bytes, do not edit.\n")

    for u in slices:
        my_labels = 1 + len(u.rows)
        if area_count >= ORIG_AREAS_PER_FILE or label_count + my_labels > ORIG_LABELS_PER_FILE:
            f.write("    END\n")
            f.close()
            file_i += 1
            area_count = 0
            label_count = 0
            f = open(getOrigAsmDir() / f"orig_{file_i:02d}.s", "w")
            f.write("; AUTOGENERATED original bytes, do not edit.\n")
        _emit_slice_asm(f, u, bin_data, text_lo)
        area_count += 1
        label_count += my_labels

    f.write("    END\n")
    f.close()

    getOrigObjDir().mkdir(parents=True, exist_ok=True)
    with open(stamp_f, "w") as sf:
        sf.write(stamp + "\n")

    slice_bytes = sum(u.end - u.start for u in slices)
    pin_bytes = sum(u.end - u.start for u in pins)
    echo (f"Original units: {len(units)} ({len(pins)} pinned, {len(slices)} slices)")
    echo (f"  pinned bytes: 0x{pin_bytes:X}, slice bytes: 0x{slice_bytes:X}")
    if not pins and not _load_known_syms():
        echo ("  (no compiled symbols known, everything keeps original bytes)")

    return True
