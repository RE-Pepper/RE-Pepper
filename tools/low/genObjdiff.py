#!/usr/bin/env python3
# generates objdiff.json + one target .o per unit.
# objdiff only takes relocatable objects, so decompiled files get a
# clone of their compiled .o with the original bytes swapped in, and
# every other map row gets a single symbol object cut from code.bin.

import json
import os
import struct
from pathlib import Path

from tools.low.glob import *
from tools.low.readSymMap import read_sym_file, MapFmt
from tools.low.readHeader import read_header, HeadType, HeadVal
from tools.pypstem._utils import getFileBuildPath

SCHEMA = "https://raw.githubusercontent.com/encounter/objdiff/main/config.schema.json"

UNKNOWN = "Unknown"

# elf constants, 32 bit LE arm
SHT_PROGBITS, SHT_SYMTAB, SHT_STRTAB, SHT_REL, SHT_NOBITS = 1, 2, 3, 9, 8
SHF_WRITE, SHF_ALLOC, SHF_EXEC = 1, 2, 4
STT_NOTYPE, STT_OBJECT, STT_FUNC = 0, 1, 2
STB_LOCAL, STB_GLOBAL, STB_WEAK = 0, 1, 2
EABI5 = 0x05000000

def _module_of(src, modules):
    # longest matching module path wins
    best = None
    for mod_path_name, mod_data in modules.items():
        mod_subdir = mod_data.get("source_dir") or "."
        if mod_subdir in (".", "", None):
            mod = mod_path_name
        else:
            mod = f"{mod_path_name}/{mod_subdir}"
        if str(src).startswith(mod) and len(mod) > len(best or ""):
            best = mod_data.get("name") or mod_path_name
    return best

def _emit_obj(path, eflags, secs, syms, relocs):
    data = _emit_obj_bytes(eflags, secs, syms, relocs)
    _write_if_changed(path, data)

def _write_if_changed(path, data):
    # skip the write when the file is already identical
    try:
        with open(path, "rb") as f:
            if f.read() == data:
                return
    except FileNotFoundError:
        pass
    with open(path, "wb") as f:
        f.write(data)

def _emit_obj_bytes(eflags, secs, syms, relocs):
    """build a 32 bit LE ARM ET_REL object image.

    secs:    content sections in order: dicts with name, type, flags,
             align, data (bytes) and size (used for SHT_NOBITS)
    syms:    non null symbols: (name, value, size, bind, type, other,
             shndx); locals must come before globals, shndx is 1 based
             into the content sections (0 = undefined)
    relocs:  {position in secs: [(offset, symbol index, r_type), ...]}
             with symbol indexes 1 based (0 is the null symbol)
    """
    secs = list(secs)
    syms = list(syms)

    # index of the first non local entry in the final symbol table
    sym_first_global = len(syms) + 1
    for i, s in enumerate(syms):
        if s[3] != STB_LOCAL:
            sym_first_global = i + 1
            break

    # section name string table (starts with the implicit null entry)
    shstrtab = bytearray(b"\x00")
    sh_names = [0]
    for s in secs:
        sh_names.append(len(shstrtab))
        shstrtab += s["name"].encode() + b"\x00"

    # one .rel section per content section that carries relocations
    rel_names, rel_data, rel_target = [], [], []
    for pos in sorted(relocs):
        name = f".rel{secs[pos]['name']}"
        sh_names.append(len(shstrtab))
        shstrtab += name.encode() + b"\x00"
        rel_names.append(name)
        rel_data.append(b"".join(
            struct.pack("<II", off, (sym_idx << 8) | rtype) for off, sym_idx, rtype in relocs[pos]
        ))
        rel_target.append(pos + 1) # 1 based section table index

    for extra in (".symtab", ".strtab", ".shstrtab"):
        sh_names.append(len(shstrtab))
        shstrtab += extra.encode() + b"\x00"

    # symbol + string table contents
    strtab = bytearray(b"\x00")
    symtab_data = bytearray(struct.pack("<IIIBBH", 0, 0, 0, 0, 0, 0))
    for name, value, size, bind, typ, other, shndx in syms:
        noff = len(strtab)
        strtab += name.encode() + b"\x00"
        symtab_data += struct.pack("<IIIBBH", noff, value, size, (bind << 4) | typ, other, shndx)

    n_content = len(secs)
    n_rel = len(rel_data)
    symtab_idx = 1 + n_content + n_rel
    strtab_idx = symtab_idx + 1
    shstrtab_idx = symtab_idx + 2

    # final section table layout: NULL, content, .rel, .symtab, .strtab, .shstrtab
    final = [(0, 0, 0, 0, None, 0)]
    for s in secs:
        data = s["data"]
        final.append((s["name"], s["type"], s["flags"], max(s["align"], 1),
                      data, len(data) if data is not None else s.get("size", 0)))
    for i in range(n_rel):
        final.append((rel_names[i], SHT_REL, 0, 4, rel_data[i], len(rel_data[i])))
    final.append((".symtab", SHT_SYMTAB, 0, 4, bytes(symtab_data), len(symtab_data)))
    final.append((".strtab", SHT_STRTAB, 0, 1, bytes(strtab), len(strtab)))
    final.append((".shstrtab", SHT_STRTAB, 0, 1, bytes(shstrtab), len(shstrtab)))

    # lay out the file body
    body = bytearray(b"\x00" * 0x34)
    offsets = []
    for name, typ, flags, align, data, size in final:
        offsets.append(len(body) if typ != SHT_NOBITS else 0)
        if typ == SHT_NOBITS or data is None:
            continue
        body += b"\x00" * ((-len(body)) % align)
        offsets[-1] = len(body)
        body += data

    sht_off = len(body) + (-len(body)) % 4

    out = bytearray()
    out += b"\x7FELF\x01\x01\x01\x00" + b"\x00" * 8
    out += struct.pack("<HHI", 1, 0x28, 1) # ET_REL, EM_ARM, version
    out += struct.pack("<III", 0, 0, sht_off)
    out += struct.pack("<I6H", eflags, 0x34, 0x20, 0, 0x28, len(final), shstrtab_idx)
    out += body[0x34:]
    out += b"\x00" * (sht_off - len(out))

    for i, (name, typ, flags, align, data, size) in enumerate(final):
        if typ == SHT_SYMTAB:
            link, info, entsize = strtab_idx, sym_first_global, 16
        elif typ == SHT_REL:
            link, info, entsize = symtab_idx, rel_target[i - 1 - n_content], 8
        else:
            link, info, entsize = 0, 0, 0
        out += struct.pack("<10I", sh_names[i], typ, flags, 0, offsets[i],
                           size, link, info, align, entsize)
    return bytes(out)

def _emit_row_obj(path, row, header, orig, name):
    """single symbol ET_REL object cut from the original binary"""
    start, end, typ = row[MapFmt.Start], row[MapFmt.End], row[MapFmt.Type]
    size = end - start
    text_start = header[HeadType.Text][HeadVal.Start]
    rw_start = header[HeadType.Rw][HeadVal.Start]
    bss_start = header[HeadType.Bss][HeadVal.Start]

    if "f" in typ:
        sec_name, sec_type, sec_flags = ".text", SHT_PROGBITS, SHF_ALLOC | SHF_EXEC
        map_sym, sym_type = "$a", STT_FUNC
    elif start >= bss_start:
        sec_name, sec_type, sec_flags = ".bss", SHT_NOBITS, SHF_ALLOC | SHF_WRITE
        map_sym, sym_type = "$d", STT_OBJECT
    elif start >= rw_start:
        sec_name, sec_type, sec_flags = ".data", SHT_PROGBITS, SHF_ALLOC | SHF_WRITE
        map_sym, sym_type = "$d", STT_OBJECT
    else:
        sec_name, sec_type, sec_flags = ".rodata", SHT_PROGBITS, SHF_ALLOC
        map_sym, sym_type = "$d", STT_OBJECT

    data = None
    if sec_type != SHT_NOBITS:
        avail = max(len(orig) - (start - text_start), 0)
        size = min(size, avail)
        data = orig[start - text_start : start - text_start + size]

    secs = [{"name": sec_name, "type": sec_type, "flags": sec_flags, "align": 4,
             "data": data, "size": size}]
    syms = [
        (map_sym, 0, 0, STB_LOCAL, STT_NOTYPE, 0, 1),
        (name, 0, size, STB_GLOBAL, sym_type, 0, 1),
    ]
    _emit_obj(path, EABI5, secs, syms, {})

def _emit_mirror_obj(path, base_o, file_rows, orig, text_start):
    """clone the compiled .o's structure, swap in original bytes"""
    from elftools.elf.elffile import ELFFile

    with open(base_o, "rb") as f:
        elf = ELFFile(f)
        eflags = elf.header["e_flags"]

        base_secs = []
        for i, sec in enumerate(elf.iter_sections()):
            base_secs.append({
                "idx": i, "name": sec.name, "type": sec["sh_type"],
                "flags": int(sec["sh_flags"]), "size": int(sec["sh_size"]),
                "align": max(int(sec["sh_addralign"]) or 4, 1),
                "data": b"" if sec["sh_type"] == "SHT_NOBITS" else sec.data(),
            })

        symtab = elf.get_section_by_name(".symtab")
        base_syms = []
        vis_map = {"STV_DEFAULT": 0, "STV_INTERNAL": 1, "STV_HIDDEN": 2, "STV_PROTECTED": 3}
        for s in symtab.iter_symbols():
            shndx = s["st_shndx"]
            if not isinstance(shndx, int):
                shndx = {"SHN_UNDEF": 0, "SHN_ABS": 0xFFF1}.get(shndx, 0xFFF1)
            other = s["st_other"]
            other = vis_map.get(other["visibility"], 0) if isinstance(other, dict) or hasattr(other, "get") else int(other)
            base_syms.append({
                "name": s.name, "value": int(s["st_value"]), "size": int(s["st_size"]),
                "bind": {"STB_LOCAL": 0, "STB_GLOBAL": 1, "STB_WEAK": 2}.get(s["st_info"]["bind"], 0),
                "type": {"STT_NOTYPE": 0, "STT_OBJECT": 1, "STT_FUNC": 2, "STT_SECTION": 3, "STT_FILE": 4}.get(s["st_info"]["type"], 0),
                "other": other, "shndx": shndx,
            })

        base_relocs = {} # target section idx -> [(offset, sym idx, type)]
        for sec in elf.iter_sections():
            if sec["sh_type"] != "SHT_REL":
                continue
            lst = base_relocs.setdefault(int(sec["sh_info"]), [])
            for r in sec.iter_relocations():
                lst.append((int(r["r_offset"]), int(r["r_info_sym"]), int(r["r_info_type"])))

    # keep only allocatable PROGBITS/NOBITS sections
    keep = [s for s in base_secs if (s["flags"] & SHF_ALLOC) and s["type"] in ("SHT_PROGBITS", "SHT_NOBITS")]
    old_to_new = {s["idx"]: 1 + i for i, s in enumerate(keep)}

    reloc_syms = set()
    for s in keep:
        for _, sym_idx, _ in base_relocs.get(s["idx"], []):
            reloc_syms.add(sym_idx)

    # filter the symbol table
    syms = []
    new_idx_of = {}
    for i, s in enumerate(base_syms):
        if s["type"] == 4: # STT_FILE
            continue
        if s["shndx"] == 0xFFF1: # absolute (build attributes etc.)
            continue
        if s["shndx"] == 0:
            if i not in reloc_syms:
                continue
            new_shndx = 0
        else:
            if s["shndx"] not in old_to_new:
                continue
            new_shndx = old_to_new[s["shndx"]]
        new_idx_of[i] = len(syms) + 1 # +1 for the null symbol
        syms.append((s["name"], s["value"], s["size"], s["bind"], s["type"], s["other"], new_shndx))

    # fill section content: original bytes for row'd symbols, base
    # placeholders back on top of relocation words
    rows_by_name = {r[MapFmt.Symbol]: r for r in file_rows}
    secs = []
    relocs = {}
    for s in keep:
        data = s["data"]
        if s["type"] != "SHT_NOBITS" and data is not None:
            buf = bytearray(data)
            for i, bs in enumerate(base_syms):
                if bs["shndx"] != s["idx"] or not bs["name"] or bs["name"] not in rows_by_name:
                    continue
                r = rows_by_name[bs["name"]]
                size = min(bs["size"] or s["size"], s["size"], r[MapFmt.End] - r[MapFmt.Start])
                size = max(min(size, len(orig) - (r[MapFmt.Start] - text_start), len(buf) - bs["value"]), 0)
                if size:
                    buf[bs["value"] : bs["value"] + size] = orig[
                        r[MapFmt.Start] - text_start : r[MapFmt.Start] - text_start + size
                    ]
            for off, _, _ in base_relocs.get(s["idx"], []):
                buf[off : off + 4] = data[off : off + 4]
            data = bytes(buf)
        secs.append({
            "name": s["name"],
            "type": SHT_PROGBITS if s["type"] == "SHT_PROGBITS" else SHT_NOBITS,
            "flags": s["flags"], "align": s["align"],
            "data": None if s["type"] == "SHT_NOBITS" else data,
            "size": s["size"],
        })
        rl = [(off, new_idx_of[si], rt) for off, si, rt in base_relocs.get(s["idx"], []) if si in new_idx_of]
        if rl:
            relocs[len(secs) - 1] = rl

    _emit_obj(path, eflags, secs, syms, relocs)

def _inputs_signature():
    # content hashed, not mtimes: the build rewrites some inputs (like
    # .syms) on every run even when nothing changed
    import hashlib
    files = [getMapFile(), getBinCodeFile(), getCfgSymsFile(), getElfFile(),
             getDataDir() / "template" / "objdiff.json", Path(__file__)]
    parts = []
    for p in files:
        if p and p.exists():
            parts.append(f"{p.name}:{hashlib.sha256(p.read_bytes()).hexdigest()[:16]}")
    return ";".join(parts)

def gen_objdiff():
    syms_file = getCfgSymsFile()
    if not getElfFile().exists():
        echo ("Skipping objdiff, build output missing.")
        return

    # the unit objects only change when the map, the binary, the symbol
    # cache or the link output changes; skip the ~half minute of tiny
    # file writes when nothing did
    stamp = getBuildPath() / "objdiff.stamp"
    sig = _inputs_signature()
    try:
        if stamp.read_text() == sig:
            echo ("Skipping objdiff, nothing changed.")
            return
    except FileNotFoundError:
        pass

    header = read_header()
    text_start = header[HeadType.Text][HeadVal.Start]
    with open(getBinCodeFile(), "rb") as f:
        orig = f.read()

    out_dir = getBuildPath() / "objdiff"
    out_dir.mkdir(parents = True, exist_ok = True)

    # compiled source files (from the .syms build cache)
    syms_files = {}
    if syms_file.exists():
        with open(syms_file, "r") as f:
            syms_files = json.load(f)

    # named rows first (aliases dedup by start, a named row wins over an
    # unnamed one at the same address), then unnamed rows as synthetic
    # units so the report totals cover the entire binary
    rows = []
    seen_starts = set()
    for named in (True, False):
        for r in read_sym_file():
            if not r[MapFmt.End] or r[MapFmt.End] <= r[MapFmt.Start]:
                continue
            if bool(r[MapFmt.Symbol]) != named:
                continue
            if r[MapFmt.Start] in seen_starts:
                continue
            seen_starts.add(r[MapFmt.Start])
            rows.append(r)
    rows_by_name = {}
    for r in rows:
        if r[MapFmt.Symbol]:
            rows_by_name.setdefault(r[MapFmt.Symbol], r)

    def row_name(r):
        if r[MapFmt.Symbol]:
            return r[MapFmt.Symbol]
        return f"fn_{r[MapFmt.Start]:08X}" if "f" in r[MapFmt.Type] else f"dat_{r[MapFmt.Start]:08X}"

    units = []
    categories = set()
    claimed = set()

    # decompiled source files: one mirror unit each
    for src, syms in sorted(syms_files.items()):
            file_rows = []
            seen = set()
            for s in syms:
                r = rows_by_name.get(s)
                if r is None or r[MapFmt.Start] in seen:
                    continue
                seen.add(r[MapFmt.Start])
                file_rows.append(r)
            if not file_rows:
                continue
            for r in file_rows:
                claimed.add(r[MapFmt.Start])

            mod = _module_of(src, cfg.modules)
            cat = mod or UNKNOWN
            categories.add(cat)

            tag = str(src).replace("/", "_").replace(".", "_")
            target_o = out_dir / f"mod_{tag}.o"
            base_o = getFileBuildPath(Path(str(getProjDir() / src)))
            _emit_mirror_obj(target_o, base_o, file_rows, orig, text_start)

            # no ctx_path: gen_ctx only runs in memory inside
            # tools/upload.py, there is no ctx file on disk to point at
            # and make.py cannot build one, so keep the scratch button
            # to platform + compiler + preset
            units.append({
                "name": f"{cat}|{src}" if mod else str(src),
                "target_path": os.path.relpath(str(target_o), getProjDir()),
                "base_path": os.path.relpath(str(base_o), getProjDir()),
                "scratch": {
                    "platform": "n3ds",
                    "compiler": "outatime",
                    "preset_id": cfg.decompme_id or 0,
                },
                "metadata": {
                    "complete": all(r[MapFmt.Rank] == "O" for r in file_rows),
                    "source_path": str(src),
                    "progress_categories": [cat],
                },
            })

    # everything else: one single-row target object, no base object
    for r in rows:
        if r[MapFmt.Start] in claimed:
            continue
        name = row_name(r)
        target_o = out_dir / f"row_{r[MapFmt.Start]:08X}.o"
        _emit_row_obj(target_o, r, header, orig, name)

        cat = UNKNOWN
        categories.add(cat)
        unit = {
            "name": name,
            "target_path": os.path.relpath(str(target_o), getProjDir()),
            "scratch": {
                "platform": "n3ds",
                "compiler": "outatime",
                "preset_id": cfg.decompme_id or 0,
                "build_ctx": False,
            },
            "metadata": {
                "complete": bool(r[MapFmt.Symbol]) and r[MapFmt.Rank] == "O",
                "progress_categories": [cat],
            },
        }
        if not r[MapFmt.Symbol]:
            # pools and orphan data blobs: count them in the report,
            # but keep them out of the sidebar
            unit["metadata"]["auto_generated"] = True
        units.append(unit)

    # template in data/template/objdiff.json, /// for the units,
    # &&& for the categories
    def render_units():
        parts = []
        for u in units:
            body = json.dumps(u, indent=8)
            parts.append(body)
        return ",\n".join(parts)

    def render_categories():
        return ",\n".join(
            json.dumps({"id": c, "name": c}, indent=8) for c in sorted(categories)
        )

    template = (getDataDir() / "template" / "objdiff.json").read_text()
    out = template.replace("///", render_units()).replace("&&&", render_categories())
    with open(getJsonObjdiffFile(), "w") as f:
        f.write(out)
    stamp.write_text(sig)
    echo (f"objdiff: {len(units)} units in {getJsonObjdiffFile().name}")
