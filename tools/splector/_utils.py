import os
import shutil
from low.__parseMap import *
from enum import IntEnum
from colorama import Fore, Style
from capstone import *

curname = ""
curstatus = "Initializing"

def set_progress(name):
    global curname
    curname = name
def set_status(status):
    global curstatus
    curstatus = status

def clear_line():
    print (' ' * shutil.get_terminal_size((80, 20)).columns, end='\r')
def print_progress():
    clear_line()
    print (Fore.LIGHTCYAN_EX + curstatus + Fore.LIGHTRED_EX + curname + Fore.RESET + Style.RESET_ALL + " ...", end='\r')

def upd_status(status):
    set_status(status)
    print_progress()

def echo(str, end="\n"):
    clear_line()
    print (str, end)

def str_addrs(addrs):
    return (", ".join(f"{a:08X}h" for a in addrs))
def str_instrs(instrs):
    return ("\n".join(f"0x{i.address:08X}: {i.mnemonic} {i.op_str}" for i in instrs))

error_list = []
error_details = ""
def error_func(f, instrs, str):
    global error_details
    error_list.append(f"ERROR! Function at 0x{f[0]:08X}: {str}")
    if error_details != "":
        return
    line=[]
    line.append(f"Details: Range: 0x{f[0]:08X} - 0x{f[1]:08X}, Name: {f[2]}, Next Func Start: {f[4]:08X}")
    line.append("instrs:")
    line.append(str_instrs(instrs))
    error_details = "\n".join(line)
def error_exec():
    global error_details

    if error_details == "":
        return

    for error in error_list:
        echo (error)
    echo (error_details)
    error_details = ""
    error_list.clear()
    quit()

def clean_dir(path):
    out_dir = os.path.dirname(path)
    if os.path.exists(out_dir):
        upd_status ("Output exists, deleting")
        shutil.rmtree(out_dir)
    os.makedirs(out_dir, exist_ok=True)

def check_name(name, typ, addr):
    if not name or name.strip() == "":
        if (typ == "f"):
            return f"fn_{addr:08X}"
        elif (typ is None or typ == ""):
            return f"unk_{addr:08X}"
        else:
            return f"dat_{addr:08X}"
    return name

def load_map():
    upd_status ("Loading map")
    sym_map = {}
    ranges = []
    syms = read_sym_file()
    symlen = len(syms)
    for i in range(symlen):
        sym = syms[i]
        start = sym[MapFmt.Start]
        end = sym[MapFmt.End]
        typ = sym[MapFmt.Type]
        next = syms[i+1][MapFmt.Start] if (i != symlen-1) else end
        name = check_name(sym[MapFmt.Symbol], typ, start) # valid name
        
        if start != 0x00100000: # skip __ctr_start
            sym_map[start] = name

        if (end > next) and (typ == "f"):
            echo (f"OVERLAP! {name} touching next symbol.")

        if sym[MapFmt.Rank] == 'O': # Matched
            continue
        if end is None or end <= 0:
            if symlen < i+1:
                echo ("Last symbol has no end.")
            elif symlen > (i+1):
                end = syms[i+1][MapFmt.Start]

        ranges.append((start, end, name, typ, next))

    ranges.sort(key=lambda x: x[0])
    return sym_map, ranges
