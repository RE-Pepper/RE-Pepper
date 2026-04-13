#!/usr/bin/env python3
import sys
import time
import shutil
import argparse
import threading
import multiprocessing
from colorama import Fore, Style

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from tools.low.updateMap import *
from tools.low.readSymMap import *
from tools.low.readElfMap import *
from tools.low.callAsmdiff import *

is_skip_mode = False
is_sim_mode = False
is_silent = False
is_log = False
do_error = False
csv_path = ""
log_path = ""

def rank_symbol(symbol, decomp_symbol):
    res, sym_size = callAsmdiff(symbol, decomp_symbol, None, True)
    if sym_size == 1:
        return 'O'
    if res is None:
        return 'U'
    if res.returncode != 0:
        fail (f"asm-differ failed:\n{res.stderr}", False)

    out = res.stdout
    if "CURRENT" not in out: raise RuntimeError(f"Unexpected output:\n{out}")

    rank = 'O'
    if "CURRENT (0)" in out:
        return rank # match override
    if "diff_change" in out:
        rank = 'm'
    if "diff_add" in out or "diff_remove" in out:
        rank = 'm' if out.count('diff_add') == out.count('diff_remove') else 'M'
    return rank

def getRankName(rank: str):
    match rank:
        case 'O':
            return Fore.GREEN + "OK" + Fore.RESET
        case 'm':
            return Fore.YELLOW + "Minor problems" + Fore.RESET
        case 'M':
            return Fore.RED + "Major problems" + Fore.RESET
        case 'U':
            return "Undecompiled"
    return '?'

def getRankMsg(prev, now):
    if now == 'O':
        if prev == 'U': return "Now perfectly Matching."
        if prev in ('m','M'): return "Now Matching."
        return "Ok."
    if now == 'U':
        if prev == 'O': return "Now completely Undefined."
        if prev in ('m','M'): return "Now Undefined."
        return "Not Decompiled."
    if now == 'M':
        if prev == 'O': return "Oops, Now Mismatching."
        if prev == 'U': return "Getting closer, now Mismatching."
        if prev == 'm': return "Made it worse, Mismatching."
        return "Still Mismatching."
    if now == 'm':
        if prev == 'O': return "Change it back, Minor Mismatch."
        if prev == 'U': return "Very close, Minor Mismatch."
        if prev == 'M': return "Getting close, Minor Mismatch."
        return "Still minor Mismatching."
    return '?'

def printf(str, end='\n'):
    if is_silent:
        return
    echo (str, end=end)

def clear_line():
    printf (' ' * shutil.get_terminal_size((80, 20)).columns, end='\r')

def print_progress(name, prog, rank):
    printf (Fore.LIGHTRED_EX + f"[{prog}%] " + Fore.LIGHTCYAN_EX + name + Fore.RESET + Style.RESET_ALL + f" ({rank})", end='\r')

def check_syms():
    syms = read_sym_file()
    newsyms = []
    sym_starts = []
    sym_ends = []
    do_rewrite = False
    is_error = False
    sym_num = len(syms)
    if sym_num == 0:
        print ("No symbols found in map.")
        return
    last_sym_addr = syms[-1][MapFmt.Start]
    first_sym_addr = syms[0][MapFmt.Start]
    last_name = ""
    log = []

    for sym in syms:
        end=sym[MapFmt.End]
        start=sym[MapFmt.Start]
        name=sym[MapFmt.Symbol]
        rank='U'

        progress = ((start - first_sym_addr) / (syms[-1][MapFmt.End] - first_sym_addr)) * 100
        progress = round(progress, 1)

        # check addr dupl
        if start in sym_starts:
            echo (f"0x{start:08X} appears more than once!")

        sym_starts.append(start)
        sym_ends.append(end)

        # check no name
        if is_skip_mode or not name or len(name) == 0:
            newsyms.append(sym)
            continue
        #continue
        # try get symbol from elf
        decomp_symbol = get_elf_symbol(name, False)
        if not decomp_symbol is None:
            rank = rank_symbol(sym, decomp_symbol)

        sect=sym[MapFmt.Section]
        pool=sym[MapFmt.Pool]
        typ=sym[MapFmt.Type]
        sectname=sym[MapFmt.SectionName]

        # main adding
        newsyms.append((start, pool, end, sect, rank, typ, name, sectname))
        last_name = name

        clear_line()
        print_progress (last_name, progress, rank)

        oldrank=sym[MapFmt.Rank]
        if oldrank != rank:
            change = f"{name} {oldrank} -> {rank} ({getRankMsg(oldrank, rank)})"
            echo (change)
            log.append(change)
            do_rewrite = True

    clear_line()

    # post check before writing
    mySyms = [(int(sym_starts[i]), int(sym_ends[i])) for i in range(len(sym_starts))]
    mySyms.sort(key=lambda x: x[0])
    for i in range(len(mySyms) - 1):
        addr, endaddr = mySyms[i]
        next_addr = mySyms[i + 1][MapFmt.Start]
        if endaddr > next_addr:
            echo (f"MAP OVERLAP: 0x{addr:08X} overlaps with 0x{next_addr:08X}")
            is_error = True

    if is_error and do_rewrite:
        echo ("Errors detected, cannot update map. Please fix!")
        if is_sim_mode or is_skip_mode:
            echo (r"... you ran in simulation mode anyways so \_(ツ)_/")
        fail ("Read above")
        return

    if is_error:
        fail ("Errors detected, but no changes. Please fix!")
        return

    if is_sim_mode or is_skip_mode:
        echo ("Simulation mode, not updating map file")
        return

    if not do_rewrite:
        echo ("Everything up to date")
        return

    if is_log:
        echo ("Writing log")
        with open(log_path, 'w') as f:
            for line in log:
                f.write(f"{line}\n")

    elif do_error:
        fail_ex ("Map has differences, chose to error.", "If this is from Github, make sure you ran tools/check.py!")

    else:
        echo ("Updating map ...")

        updateFull(newsyms, csv_path)

def check_sym(symbol_name):
    dec = get_elf_symbol(symbol_name)
    if dec is None:
        echo (f"Symbol {symbol_name} not found in build.")
        return

    symbol_name = dec[ElfMapFmt.Symbol]
    sym = get_symbol(symbol_name)
    if sym is None:
        echo (f"Symbol {symbol_name} not found in map.")
        return

    prevrank = sym[MapFmt.Rank]
    nowrank = rank_symbol(sym, dec)

    if prevrank != nowrank:
        sym = list(sym)
        sym[MapFmt.Rank] = nowrank
        updateSingle(sym, csv_path)

        echo (f"{prevrank} -> {nowrank} ({getRankMsg(prevrank, nowrank)})")
    elif prevrank == "O":
        printf ("Still matching")
    else:
        printf (f"Unchanged. ({prevrank})")

def main():
    global csv_path
    global log_path
    global is_skip_mode
    global is_sim_mode
    global is_silent
    global is_log
    global do_error

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", action="store_true", help="Skip rank checking (fast)")
    parser.add_argument("-s", action="store_true", help="Simulation mode (don't write file)")
    parser.add_argument("-q", action="store_true", help="Dont print progress")
    parser.add_argument("-w", action="store_true", help="Log changes to file (No csv update)")
    parser.add_argument("-e", action="store_true", help="Error when map has differences.")
    parser.add_argument("sym", nargs="?", help="Only check this symbol")
    args = parser.parse_args()

    is_skip_mode = args.f
    is_sim_mode = args.s
    is_silent = args.q
    is_log = args.w
    do_error = args.e

    csv_path = getMapFile()
    log_path = str(getVerDir() / ".changes")

    if cfg.only_matching:
        csv_path = getMapFile().with_stem(f"{getMapFile().stem}_test")
        echo ("Info: TEST MODE. You need to compile without -m (only matching) to rebuild the functions map. This output will be written to data/*_test.csv")

    if args.sym:
        check_sym(args.sym)
    else:
        start = time.time()
        check_syms()
        clear_line()
        echo (f"{int(time.time() - start)}s elapsed")

if __name__ == "__main__":
    main()

