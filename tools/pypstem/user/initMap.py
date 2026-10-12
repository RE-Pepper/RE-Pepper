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
    off = start - text_lo
    for insn in md.disasm(data[off:off + MAX_FUNC], start):
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
                break
        elif insn.id == ARM_INS_POP:
            break

def scan_pointers(data, lo, hi, text_lo, text_hi, thumb, funcs):
    # vtable and jump table entries in ro/rw point into text. a run of
    # consecutive words with targets clustered in one small window is a
    # switch table pointing mid function, everything else is a good
    # function guess (vtable slots spread over the whole text)
    run = []
    for a in range(lo, hi - 3, 4):
        w = int.from_bytes(data[a - text_lo:a - text_lo + 4], "little")
        ok = text_lo <= w < text_hi and ((w & 1) == (1 if thumb else 0) or (w & 3) == 0)
        if ok:
            run.append((a, w & ~1))
            continue
        _flush_run(run, funcs)
        run = []
    _flush_run(run, funcs)

def _flush_run(run, funcs):
    if len(run) >= 3 and (max(w for _, w in run) - min(w for _, w in run)) < 0x1000:
        return # switch table, targets are mid function
    for _, w in run:
        funcs.add(w)

def detect(data, text_lo, text_hi, ro_lo, rw_lo, rw_hi, thumb):
    md = disas_mode(thumb)
    funcs = {text_lo}
    done = set()
    todo = [text_lo]
    while todo:
        f = todo.pop()
        if f in done or not (text_lo <= f < text_hi):
            continue
        done.add(f)
        scan_func(md, data, text_lo, text_hi, f, thumb, funcs)
        todo.extend(x for x in funcs if x not in done)
    # data references expand the graph, then scan those too
    before = set(funcs)
    if ro_lo < rw_hi:
        scan_pointers(data, ro_lo, max(rw_hi, ro_lo), text_lo, text_hi, thumb, funcs)
        todo.extend(x for x in funcs if x not in done)
        while todo:
            f = todo.pop()
            if f in done or not (text_lo <= f < text_hi):
                continue
            done.add(f)
            scan_func(md, data, text_lo, text_hi, f, thumb, funcs)
            todo.extend(x for x in funcs if x not in done)
    return sorted(x for x in funcs if text_lo <= x < text_hi)

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
    if not getBinCodeFile().exists():
        fail_ex (f"Version '{ver}' is missing code.bin or exh.bin.", str(getVerDir(ver)), False)
    if not getHeadFile().exists():
        fail_ex (f"Version '{ver}' is missing exh.bin.", str(getVerDir(ver)), False)

    header = read_header()
    text_lo = header[HeadType.Text][HeadVal.Start]
    text_hi = header[HeadType.Text][HeadVal.End]
    ro_lo = header[HeadType.Ro][HeadVal.Start]
    rw_lo = header[HeadType.Rw][HeadVal.Start]
    rw_hi = header[HeadType.Rw][HeadVal.End]
    data = getBinCodeFile().read_bytes()

    if args.thumb:
        thumb = True
    elif args.arm:
        thumb = False
    else:
        thumb = entry_score(data, text_lo, True) > entry_score(data, text_lo, False)
    echo (f"Decoding as {'thumb' if thumb else 'arm'}")

    funcs = detect(data, text_lo, text_hi, ro_lo, rw_lo, rw_hi, thumb)
    echo (f"Found {len(funcs)} functions, last at 0x{funcs[-1]:08X}")

    syms = []
    for i, f in enumerate(funcs):
        end = funcs[i + 1] if i + 1 < len(funcs) else text_hi
        syms.append((f, None, end, None, "U", "f", "", ""))
    updateFull(syms, getMapFile(ver))
    echo (f"Wrote {getMapFile(ver)}")

if __name__ == "__main__":
    main()
