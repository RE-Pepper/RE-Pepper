#!/usr/bin/env python3
# creates the initial map.csv for a version: function boundaries from a
# call scan over code.bin, seeded at the entry point. rows stay unnamed
# with rank U, names and data rows get added later during decompilation.
#
# usage: python3 tools/pypstem/user/initMap.py <version> [--overwrite]
#                                              [--thumb] [--arm]

import sys
import argparse
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[3]))

from tools.low.glob import *
from tools.low.readHeader import *
from tools.low.readSymMap import MapFmt
from tools.low.updateMap import updateFull
from tools.low.utilsPrint import *

from capstone import *
from capstone.arm import *

MAX_FUNC = 0x20000

def disas_mode(thumb):
    md = Cs(CS_ARCH_ARM, CS_MODE_THUMB if thumb else CS_MODE_ARM)
    md.detail = True
    return md

def pool_addr(insn, thumb):
    # ldr rX, [pc, #imm]: address of the literal pool word
    for op in insn.operands:
        if op.type == ARM_OP_MEM and op.mem.base == ARM_REG_PC:
            base = (insn.address + 4) & ~3 if thumb else insn.address + 8
            return base + op.mem.disp
    return None

def scan_func(md, data, text_lo, text_hi, start, thumb, funcs):
    # walk one function, collecting call targets and pool pointers.
    # bl targets are sure functions, pool words pointing into text are
    # good guesses (vtables, jump tables). a plain b is not evidence.
    # returns the end of the last decoded instruction (pool starts there)
    off = start - text_lo
    code_end = start
    first_ret = None
    for insn in md.disasm(data[off:off + MAX_FUNC], start):
        code_end = insn.address + insn.size
        if insn.id in (ARM_INS_BL, ARM_INS_BLX) and insn.operands:
            op = insn.operands[0]
            if op.type == ARM_OP_IMM:
                t = op.imm & ~1
                if text_lo <= t < text_hi:
                    funcs.add(t)
        elif insn.id == ARM_INS_LDR:
            pa = pool_addr(insn, thumb)
            if pa is None or not (text_lo <= pa <= text_hi - 4):
                continue
            word = int.from_bytes(data[pa - text_lo:pa - text_lo + 4], "little")
            if text_lo <= word < text_hi and (word & 1) == (1 if thumb else 0):
                funcs.add(word & ~1)
        elif insn.id == ARM_INS_B:
            if insn.cc == ARM_CC_AL:
                # tail call: the target is a function when it opens with
                # a prologue, a local jump does not
                if insn.operands and insn.operands[0].type == ARM_OP_IMM:
                    t = insn.operands[0].imm & ~1
                    if text_lo <= t < text_hi and is_prologue(data, text_lo, t):
                        funcs.add(t)
                break
        elif insn.id in (ARM_INS_POP, ARM_INS_BX):
            # the first return ends the code: the pool follows. keep
            # walking, later blocks still carry call targets
            if first_ret is None:
                first_ret = insn.address + insn.size
    return first_ret if first_ret is not None else code_end

def scan_init_array(data, text_lo, text_hi, funcs):
    # the .init_array table sits at the end of text: every word has the
    # top byte 0xff and encodes target = slot + word (self relative)
    slot = text_hi - 4
    while slot >= text_lo:
        w = int.from_bytes(data[slot - text_lo:slot - text_lo + 4], "little")
        if (w >> 24) != 0xFF:
            break
        t = (slot + w) & 0xFFFFFFFF
        if text_lo <= t < text_hi:
            funcs.add(t)
        slot -= 4

def scan_pointers(data, lo, hi, text_lo, text_hi, thumb, funcs):
    # vtable and jump table entries in ro/rw point into text. a run of
    # consecutive words with targets clustered in one small window is a
    # switch table pointing mid function, everything else is a good
    # function guess (vtable slots spread over the whole text)
    run = []
    in_text = lo >= text_lo and hi <= text_hi
    for a in range(lo, hi - 3, 4):
        w = int.from_bytes(data[a - text_lo:a - text_lo + 4], "little")
        # arm targets are word aligned, thumb targets carry bit0
        ok = text_lo <= w < text_hi and (w & 3) == 0 if not thumb else text_lo <= w < text_hi and (w & 1) == 1
        if ok:
            run.append((a, w & ~1))
            continue
        _flush_run(run, funcs, data, text_lo, in_text)
        run = []
    _flush_run(run, funcs, data, text_lo, in_text)

def is_prologue(data, text_lo, t):
    # arm functions open with push {..., lr} (stmdb sp!)
    w = int.from_bytes(data[t - text_lo:t - text_lo + 4], "little")
    return (w >> 16) == 0xE92D

def _flush_run(run, funcs, data=None, text_lo=None, in_text=False):
    # pointer runs outside text are vtables and callback tables: every
    # target is a function start. inside text a clustered run is a
    # jump table whose targets sit mid function - rescue only the ones
    # landing on a function prologue.
    if in_text and len(run) >= 3 and (max(w for _, w in run) - min(w for _, w in run)) < 0x1000:
        if data is not None:
            for _, w in run:
                if text_lo <= w and is_prologue(data, text_lo, w):
                    funcs.add(w)
        return
    for _, w in run:
        funcs.add(w)

def detect(data, text_lo, text_hi, ro_lo, rw_lo, rw_hi, thumb):
    md = disas_mode(thumb)
    code_ends = {}
    funcs = {text_lo}
    done = set()
    todo = [text_lo]
    while todo:
        f = todo.pop()
        if f in done or not (text_lo <= f < text_hi):
            continue
        done.add(f)
        code_ends[f] = scan_func(md, data, text_lo, text_hi, f, thumb, funcs)
        todo.extend(x for x in funcs if x not in done)
    scan_init_array(data, text_lo, text_hi, funcs)
    # data references expand the graph, then scan those too
    if ro_lo < rw_hi:
        scan_pointers(data, ro_lo, max(rw_hi, ro_lo), text_lo, text_hi, thumb, funcs)
        todo.extend(x for x in funcs if x not in done)
        while todo:
            f = todo.pop()
            if f in done or not (text_lo <= f < text_hi):
                continue
            done.add(f)
            code_ends[f] = scan_func(md, data, text_lo, text_hi, f, thumb, funcs)
            todo.extend(x for x in funcs if x not in done)
    return sorted(x for x in funcs if text_lo <= x < text_hi), code_ends


# ---------------------------------------------------------------------------
# axf/elf route: symbols replace the call scan. every FUNC/OBJECT symbol
# in the original axf becomes a row (names included when the file has
# them), the isa comes from the mapping symbols, custom input sections
# land as block rows.

SKIP_SYM = ("$", "i.", "__ARM", "BuildAttributes", "Lib$$Request", "[Anonymous")

def parse_elf(data):
    # elf32 walk: output sections and the symbol table
    import struct
    e_shoff = struct.unpack_from("<I", data, 0x20)[0]
    e_shentsize, e_shnum, e_shstrndx = struct.unpack_from("<HHH", data, 0x2E)
    shdrs = [struct.unpack_from("<IIIIII", data, e_shoff + i * e_shentsize) for i in range(e_shnum)]
    st = data[shdrs[e_shstrndx][4]:shdrs[e_shstrndx][4] + shdrs[e_shstrndx][5]]
    def nm(o):
        end = st.find(b"\0", o)
        return st[o:end].decode("utf-8", "replace")
    sections = []
    for n, typ, flags, addr, off, size in shdrs:
        sections.append((nm(n), typ, addr, off, size, flags))  # typ 8 = NOBITS
    stro = strsize = 0
    for n, typ, flags, addr, off, size in shdrs:
        if n != 0 and nm(n) == ".strtab":
            stro, strsize = off, size
    strtab = data[stro:stro + strsize]
    syms, maps = [], {}
    for n, typ, flags, addr, off, size in shdrs:
        if n == 0 or nm(n) != ".symtab":
            continue
        for i in range(size // 16):
            o = off + i * 16
            st_name, st_value, st_size, st_info, st_other, st_shndx = struct.unpack_from("<IIIBBH", data, o)
            end = strtab.find(b"\0", st_name)
            name = strtab[st_name:end].decode("utf-8", "replace")
            if not name:
                continue
            if name.startswith("$"):
                maps[st_value] = name[1]
                continue
            syms.append((st_value, st_size, st_info & 0xF, st_shndx, name))
    return sections, syms, maps

def axf_rows(data):
    sections, syms, maps = parse_elf(data)
    import bisect
    map_addrs = sorted(maps)

    def is_thumb(start):
        # the function's own mapping symbol decides (armasm emits one
        # per function start); thumb bit0 of the symbol value agrees
        i = bisect.bisect_right(map_addrs, start) - 1
        return i >= 0 and maps[map_addrs[i]] == "t"

    # one row per address: aliases collapse, functions win over data
    by_addr = {}
    for value, size, itype, shndx, name in syms:
        if name.startswith(SKIP_SYM):
            continue
        start = value & ~1
        cur = by_addr.get(start)
        if cur is None or (cur[2] != 2 and itype == 2):
            by_addr[start] = (size, itype, name, shndx)

    starts = sorted(by_addr)
    rows = []
    for i, start in enumerate(starts):
        size, itype, name, shndx = by_addr[start]
        end = start + size if size else (starts[i + 1] if i + 1 < len(starts) else start)
        if end <= start:
            end = starts[i + 1] if i + 1 < len(starts) else start + 4
        if itype == 2:  # FUNC
            rows.append([start, 0, end, "", "U", "ff" if is_thumb(start) else "f", name, ""])
        elif itype == 1:  # OBJECT
            nobits = shndx < len(sections) and sections[shndx][1] == 8
            write = shndx < len(sections) and (sections[shndx][5] & 1)
            kind = "db" if nobits else ("d" if write else "dc")
            rows.append([start, 0, end, "", "U", kind, name, ""])

    # custom input/output sections with no data symbol inside: one
    # block row each, the SectionName column carries the section (a
    # function inside the section does not cover its data, like the
    # .init_array walker above its table)
    data_starts = {r[0] for r in rows if r[5] != "f" and r[5] != "ff"}
    for name, typ, addr, off, size, flags in sections:
        if typ == 8 or size <= 0 or addr == 0:
            continue
        if name.startswith(("i.", ".text", "STUP_ENTRY")):
            continue
        covered = any(addr <= s < addr + size for s in data_starts)
        if covered:
            continue
        kind = "d" if (flags & 1) else "dc"
        rows.append([addr, 0, addr + size, "", "U", kind, "", name])

    rows.sort(key=lambda r: r[0])
    return rows

def entry_score(data, text_lo, thumb):
    # which mode decodes the entry more plausibly
    md = disas_mode(thumb)
    n = 0
    for insn in md.disasm(data[:0x400], text_lo):
        if insn.id in (ARM_INS_BL, ARM_INS_B, ARM_INS_BX, ARM_INS_PUSH, ARM_INS_LDR):
            n += 1
    return n

def main():
    parser = argparse.ArgumentParser(description="Create the initial map.csv")
    parser.add_argument("version", help="Version to initialize")
    parser.add_argument("--overwrite", action="store_true", help="Replace an existing map.csv")
    parser.add_argument("--axf", action="store_true", help="Build the map from game.axf symbols instead of a code.bin call scan")
    parser.add_argument("--thumb", action="store_true", help="Force thumb decoding")
    parser.add_argument("--arm", action="store_true", help="Force arm decoding")
    args = parser.parse_args()

    ver = args.version
    if ver not in cfg.versions:
        fail_ex (f"Version '{ver}' is not registered.", "Add it to the versions dict in data/config.user.json first.", False)
    if not getVerDir(ver).is_dir():
        fail_ex (f"Version '{ver}' has no folder.", f"Create data/ver/{ver}/ with code.bin and exh.bin.", False)
    if getMapFile(ver).exists() and not args.overwrite:
        fail_ex (f"{getMapFile(ver)} already exists.", "Pass --overwrite to replace it.", False)

    setVersion(ver)
    use_axf = args.axf
    if not use_axf and getBinAxfFile(ver).exists():
        echo ("game.axf present - pass --axf to build the map from its symbols")
    if use_axf:
        if not getBinAxfFile(ver).exists():
            fail_ex (f"Version '{ver}' has no game.axf for the symbol route.", str(getVerDir(ver)), False)
    else:
        if not getBinCodeFile().exists():
            fail_ex (f"Version '{ver}' is missing code.bin.", str(getVerDir(ver)), False)
        if not getHeadFile().exists():
            fail_ex (f"Version '{ver}' is missing exh.bin.", str(getVerDir(ver)), False)

    header = read_header()
    text_lo = header[HeadType.Text][HeadVal.Start]
    text_hi = header[HeadType.Text][HeadVal.End]
    ro_lo = header[HeadType.Ro][HeadVal.Start]
    rw_lo = header[HeadType.Rw][HeadVal.Start]
    rw_hi = header[HeadType.Rw][HeadVal.End]
    if use_axf:
        rows = axf_rows(getBinAxfFile(ver).read_bytes())
        named = sum(1 for r in rows if r[MapFmt.Symbol])
        thumb = sum(1 for r in rows if r[MapFmt.Type] == "ff")
        echo (f"axf route: {len(rows)} rows, {named} named, {thumb} thumb")
        updateFull(rows, getMapFile(ver))
        echo (f"Wrote {getMapFile(ver)}")
        return

    data = getBinCodeFile().read_bytes()

    if args.thumb:
        thumb = True
    elif args.arm:
        thumb = False
    else:
        thumb = entry_score(data, text_lo, True) > entry_score(data, text_lo, False)
    echo (f"Decoding as {'thumb' if thumb else 'arm'}")

    funcs, code_ends = detect(data, text_lo, text_hi, ro_lo, rw_lo, rw_hi, thumb)
    echo (f"Found {len(funcs)} functions, last at 0x{funcs[-1]:08X}")

    syms = []
    for i, f in enumerate(funcs):
        end = funcs[i + 1] if i + 1 < len(funcs) else text_hi
        # eu pool semantics: Pool = end of the code, End covers the pool
        code_end = code_ends.get(f, f)
        pool = (code_end + 3) & ~3
        syms.append((f, pool if pool < end else None, end, None, "U", "ff" if thumb else "f", "", ""))
    updateFull(syms, getMapFile(ver))
    echo (f"Wrote {getMapFile(ver)}")

if __name__ == "__main__":
    main()
