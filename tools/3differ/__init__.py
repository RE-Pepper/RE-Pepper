#!/usr/bin/env python3
# 3differ: 3ds focused symbol differ. no devkitpro, no objdump, pure
# capstone, works on linux and windows.
# - arm + thumb functions (auto detected), literal pools as data
# - data symbols: word diff with address normalization
# - image pointing operands are normalized to map symbols, so a shift
#   from something else growing does not zero the score
# - only the diff by default, --full prints the whole function
# - colors on a tty, plain when piped

import re
from pathlib import Path

from tools.low.glob import *
from tools.low.readSymMap import MapFmt, read_sym_file
from tools.low.readHeader import *

try:
    from capstone import *
    from capstone.arm import *
    HAS_CAPSTONE = True
except ImportError:
    HAS_CAPSTONE = False

IMG_LO = None
IMG_HI = None

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
DIM = "\033[2m"
RESET = "\033[0m"

class DiffResult:
    def __init__(self, returncode=0, stdout=""):
        self.returncode = returncode
        self.stdout = stdout

def _image_range():
    global IMG_LO, IMG_HI
    if IMG_LO is None:
        header = read_header()
        IMG_LO = header[HeadType.Text][HeadVal.Start]
        IMG_HI = header[HeadType.Bss][HeadVal.End]
    return IMG_LO, IMG_HI

# ---------------------------------------------------------------------------
# normalization: every image address becomes its map symbol

_sym_by_addr = None

def _load_symbols():
    global _sym_by_addr
    if _sym_by_addr is not None:
        return _sym_by_addr
    lo, hi = _image_range()
    table = {}
    for r in read_sym_file():
        s = r[MapFmt.Start]
        if lo <= s < hi and r[MapFmt.Symbol]:
            table[s] = r[MapFmt.Symbol]
    _sym_by_addr = table
    return table

def _norm_value(v):
    lo, hi = _image_range()
    if lo <= v < hi:
        syms = _load_symbols()
        if v in syms:
            return syms[v]
        return f"<img+0x{v - lo:X}>"
    return None

# ---------------------------------------------------------------------------
# elf reader for the built side

def _elf_sections(data):
    import struct
    if data[:4] != b"\x7fELF":
        return None
    is64 = data[4] == 2
    if is64:
        e_shoff = struct.unpack_from("<Q", data, 0x28)[0]
        e_shentsize, e_shnum, e_shstrndx = struct.unpack_from("<HHH", data, 0x3A)
    else:
        e_shoff = struct.unpack_from("<I", data, 0x20)[0]
        e_shentsize, e_shnum, e_shstrndx = struct.unpack_from("<HHH", data, 0x2E)

    shdrs = []
    for i in range(e_shnum):
        off = e_shoff + i * e_shentsize
        if is64:
            name, typ, flags, addr, offset, size = struct.unpack_from("<IIQQQQ", data, off)
        else:
            name, typ, flags, addr, offset, size = struct.unpack_from("<IIIIII", data, off)
        shdrs.append((name, typ, addr, offset, size))

    if not (0 <= e_shstrndx < len(shdrs)):
        return None
    strtab = shdrs[e_shstrndx]
    blob = data[strtab[3]:strtab[3] + strtab[4]]

    out = []
    for name, typ, addr, offset, size in shdrs:
        end = blob.find(b"\0", name)
        nm = blob[name:end].decode("utf-8", "replace") if end >= 0 else ""
        out.append((nm, typ, addr, offset, size))
    return out

def _elf_symtab(data):
    # {name: (addr, size)} and mapping symbols {addr: "a"/"t"/"d"}
    import struct
    secs = _elf_sections(data)
    if secs is None:
        return {}, {}
    syms = {}
    maps = {}
    for nm, typ, addr, offset, size in secs:
        if nm != ".symtab":
            continue
        str_off = str_size = 0
        for n2, t2, a2, o2, s2 in secs:
            if n2 == ".strtab":
                str_off, str_size = o2, s2
        strtab = data[str_off:str_off + str_size]
        for i in range(size // 16):
            o = offset + i * 16
            st_name, st_value, st_size, st_info, st_other, st_shndx = struct.unpack_from("<IIIBBH", data, o)
            if not st_name:
                continue
            end = strtab.find(b"\0", st_name)
            name = strtab[st_name:end].decode("utf-8", "replace")
            if name.startswith("$a"):
                maps[st_value] = "a"
            elif name.startswith("$t"):
                maps[st_value] = "t"
            elif name.startswith("$d"):
                maps[st_value] = "d"
            syms[name] = (st_value, st_size, st_shndx)
    return syms, maps

def _elf_section_bytes_at(data, shndx, vaddr):
    # the whole rest of the section from vaddr: with --split_sections the
    # section is the function AND its literal pool, the symbol size
    # covers only the code
    import struct
    secs = _elf_sections(data)
    if secs is None or not (0 < shndx < len(secs)):
        return None
    nm, typ, addr, offset, size = secs[shndx]
    if typ == 8:
        return None
    if not (addr <= vaddr < addr + size):
        return None
    return data[offset + (vaddr - addr): offset + size]

def _elf_bytes_at(data, vaddr, size):
    for nm, typ, addr, offset, sec_size in _elf_sections(data):
        if typ == 8: # NOBITS
            continue
        if addr <= vaddr < addr + sec_size:
            take = min(size, addr + sec_size - vaddr)
            return data[offset + (vaddr - addr): offset + (vaddr - addr) + take]
    return None

# ---------------------------------------------------------------------------
# disassembly with normalization and branch arrows

def _replace_hex(text, val, repl, count=1):
    for form in (f"#0x{val:x}", f"#0x{val:X}", f"#{val}"):
        if form in text:
            return text.replace(form, repl, count)
    return text

class Insn:
    __slots__ = ("addr", "bhex", "text", "branch_from", "branch_to")
    def __init__(self, addr, bhex, text):
        self.addr = addr
        self.bhex = bhex
        self.text = text
        self.branch_from = None # offset within the unit
        self.branch_to = None

def _normalize(insn, thumb, unit_start):
    text = f"{insn.mnemonic} {insn.op_str}".rstrip()

    if insn.id in (ARM_INS_B, ARM_INS_BL, ARM_INS_BLX, ARM_INS_BX):
        for op in insn.operands:
            if op.type == ARM_OP_IMM:
                target = op.imm & ~1
                nv = _norm_value(target)
                if nv:
                    text = _replace_hex(text, op.imm, nv)
                return text, target - unit_start
        return text, None

    if insn.id == ARM_INS_LDR and len(insn.operands) == 2:
        op = insn.operands[1]
        if op.type == ARM_OP_MEM and op.mem.base == ARM_REG_PC:
            return text, None # pool word, handled after disassembly

    for op in insn.operands:
        if op.type == ARM_OP_IMM:
            nv = _norm_value(op.imm)
            if nv:
                text = _replace_hex(text, op.imm, f"={nv}")
        elif op.type == ARM_OP_MEM and op.mem.base == ARM_REG_PC:
            base = (insn.address + 4) & ~3 if thumb else insn.address + 8
            target = base + op.mem.disp
            nv = _norm_value(target)
            if nv:
                text = _replace_hex(text, op.mem.disp, f"={nv}")
    return text, None

def _disas_unit(data_bytes, addr, thumb, code_end=None):
    md = Cs(CS_ARCH_ARM, CS_MODE_THUMB if thumb else CS_MODE_ARM)
    md.detail = True
    out = []
    branch_to = set()
    for insn in md.disasm(data_bytes[: code_end - addr if code_end else None], addr):
        text, brel = _normalize(insn, thumb, addr)
        e = Insn(insn.address, insn.bytes.hex(), text)
        if brel is not None:
            if 0 <= brel < len(data_bytes) and (code_end is None or addr + brel < code_end):
                e.branch_from = brel
                branch_to.add(brel)
            else:
                e.branch_from = None
        out.append(e)
    for e in out:
        if e.addr - addr in branch_to:
            e.branch_to = True
    return out, branch_to

def _dcd_lines(raw, addr, base_off=0):
    out = []
    for off in range(0, len(raw) - 3, 4):
        word = int.from_bytes(raw[off:off + 4], "little")
        nv = _norm_value(word)
        text = f"dcd {nv}" if nv else f"dcd 0x{word:08X}"
        out.append(Insn(addr + off, raw[off:off + 4].hex(), text))
    return out

def _find_pool(insns):
    # words after the last unconditional return are literal pool
    last = -1
    for i, e in enumerate(insns):
        t = e.text.split()[0] if e.text else ""
        if t in ("bx", "pop", "ldm") or e.text.startswith("bx lr"):
            last = i
    return insns[last + 1].addr if last >= 0 and len(insns) > last + 1 else None

# ---------------------------------------------------------------------------
# alignment

def _align(at, bt):
    import difflib
    sm = difflib.SequenceMatcher(a=[x.text for x in at], b=[x.text for x in bt], autojunk=False)
    out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                out.append(("=", at[i1 + k]))
        elif tag == "replace":
            for k in range(max(i2 - i1, j2 - j1)):
                l = at[i1 + k] if k < i2 - i1 else None
                r = bt[j1 + k] if k < j2 - j1 else None
                if l and r:
                    out.append(("c", l, r))
                elif l:
                    out.append(("d", l))
                else:
                    out.append(("a", r))
        elif tag == "delete":
            for k in range(i1, i2):
                out.append(("d", at[k]))
        elif tag == "insert":
            for k in range(j1, j2):
                out.append(("a", bt[k]))
    return out

def _gutter(e, unit_start, is_branch_target):
    pad = " "
    if e.branch_to:
        pad = "└─"
    elif e.branch_from is not None:
        pad = "├─"
    return f"{e.addr:08X} {pad} {e.text}"

# ---------------------------------------------------------------------------
# the differ

def diff_symbol(map_row, built_path=None, thumb_hint=None, color=None, full=False):
    if not HAS_CAPSTONE:
        return DiffResult(1, "3differ: capstone is missing (pip install capstone)")

    import sys
    if color is None:
        color = sys.stdout.isatty()

    lo, hi = _image_range()
    t_start = map_row[MapFmt.Start]
    t_end = map_row[MapFmt.End]
    if not t_end or t_end <= t_start:
        return DiffResult(1, "3differ: target row has no size")
    t_size = t_end - t_start
    name = map_row[MapFmt.Symbol] or f"0x{t_start:08X}"

    orig = getBinCodeFile().read_bytes()
    t_bytes = orig[t_start - lo: t_start - lo + t_size]

    if built_path is None:
        built_path = getElfFile()
    if not Path(built_path).exists():
        return DiffResult(1, "3differ: build output missing, link first")
    built = Path(built_path).read_bytes()
    bsyms, bmaps = _elf_symtab(built)
    if name not in bsyms:
        return DiffResult(1, f"3differ: {name} not found in build")
    b_addr, b_sym_size, b_shndx = bsyms[name]
    b_bytes = _elf_section_bytes_at(built, b_shndx, b_addr)
    if b_bytes is None:
        if b_sym_size == 0:
            b_sym_size = t_size
        b_bytes = _elf_bytes_at(built, b_addr, b_sym_size)
    if not b_bytes:
        return DiffResult(1, "3differ: cannot read built bytes")
    b_size = len(b_bytes)

    # data rows: no disassembly, word diff with normalization
    is_data = "f" not in (map_row[MapFmt.Type] or "")
    if is_data:
        tl = _dcd_lines(t_bytes, t_start)
        bl = _dcd_lines(b_bytes, b_addr)
    else:
        t_pool = map_row[MapFmt.Pool]
        if not t_pool or t_pool <= t_start or t_pool >= t_end:
            t_pool = None
        t_thumb = _mode_for_target(t_bytes, t_start, thumb_hint)
        b_thumb = _mode_for_built(b_bytes, b_addr, bmaps, thumb_hint if thumb_hint is not None else t_thumb)

        tl, _ = _disas_unit(t_bytes, t_start, t_thumb, t_pool)
        if not t_pool:
            p = _find_pool(tl)
            if p:
                t_pool = p
        if t_pool:
            tl = tl[: len([x for x in tl if x.addr < t_pool])]
            tl += _dcd_lines(t_bytes[t_pool - t_start:], t_pool)

        bl, _ = _disas_unit(b_bytes, b_addr, b_thumb)
        b_pool = _find_pool(bl)
        if b_pool:
            bl = bl[: len([x for x in bl if x.addr < b_pool])]
            bl += _dcd_lines(b_bytes[b_pool - b_addr:], b_pool)

    out = []
    diffs = 0
    out.append(f"target {name} @0x{t_start:08X} (size 0x{t_size:X})")
    out.append(f"built  {name} @0x{b_addr:08X} (size 0x{b_size:X})")
    out.append("")

    def C(col, s):
        return f"{col}{s}{RESET}" if color else s

    for item in _align(tl, bl):
        kind = item[0]
        if kind == "=":
            if full:
                out.append(C(DIM, f"        {item[1].addr:08X}     {item[1].text}"))
        elif kind == "c":
            out.append(C(GREEN, f"diff_change {item[1].addr:08X}     {item[1].text}"))
            out.append(C(GREEN, f"CURRENT  {item[1].addr:08X}     {item[1].text}"))
            out.append(C(RED,   f"BASE    {item[2].addr:08X}     {item[2].text}"))
            diffs += 1
        elif kind == "d":
            out.append(C(RED, f"diff_remove {item[1].addr:08X}     {item[1].text}"))
            diffs += 1
        elif kind == "a":
            out.append(C(YELLOW, f"diff_add    {item[1].addr:08X}     {item[1].text}"))
            diffs += 1

    out.append("")
    out.append(f"CURRENT ({diffs})")
    if diffs == 0:
        out.append("MATCH")
    # rc 0 also when there are diffs: a diff is not a tool failure
    # (tools/check.py treats nonzero as an error). the cli wrapper maps
    # this to a nonzero exit for humans.
    return DiffResult(0, "\n".join(out))

def _mode_for_target(data_bytes, addr, thumb_hint=None):
    if thumb_hint is not None:
        return thumb_hint
    return False # 3ds retail images are arm by default, auto thumb later

def _mode_for_built(data_bytes, addr, maps, thumb_hint=None):
    if thumb_hint is not None:
        return thumb_hint
    if maps:
        best = None
        for a, kind in maps.items():
            if a <= addr and (best is None or a > best[0]):
                best = (a, kind)
        if best:
            return best[1] == "t"
    return False
