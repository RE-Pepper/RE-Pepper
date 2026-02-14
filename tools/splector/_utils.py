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

def echo(str, end="\r"):
    clear_line()
    print (str, end)

def str_addr(a):
    return f"{a:08X}h"
def str_addrs(addrs):
    return (", ".join(str_addr(a) for a in addrs))
def str_instr(i):
    return f"0x{i.address:08X}: {i.mnemonic} {i.op_str}"
def str_instrs(instrs):
    return ("\n".join(str_instr(i) for i in instrs))
def str_func(f):
    return f"0x{f[0]:08X}-0x{f[1]:08X}: {f[2]} ({str(f[3])}) > 0x{f[4]:08X} ? {f[5]}"

error_list = []
error_details = ""
def error_func(f, instrs, str):
    global error_details
    error_list.append(f"ERROR! Function at 0x{f[0]:08X} : {str}")
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
    if not name or name.strip() == "" or "::" in name:
        if (typ == "f"):
            return f"fn_{addr:08X}", True
        elif (typ is None or typ == ""):
            return f"unk_{addr:08X}", True
        else:
            return f"dat_{addr:08X}", True
    return name, False

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
        is_data = sym[MapFmt.Type].startswith("d")

        name, is_gen = check_name(sym[MapFmt.Symbol], typ, start) # valid name

        if i < (symlen-1):
            next_any = syms[i+1][MapFmt.Start]
        else:
            next_any = end

        if end is None or end <= start:
            if symlen == i+1:
                fail ("Last symbol has no end.")
            elif symlen > (i+1):
                end = next_any

        if i < (symlen-1):
            if is_data:
                next = next_any
            else:
                next = 0
                if syms[i+1][MapFmt.Type].startswith("f"):
                    next = next_any
                else:
                    for s in syms[i+1:]:
                        if s[MapFmt.Type].startswith("f"):
                            next = s[MapFmt.Start]
                            break
                if next == 0:
                    if next_any <= start:
                        next = end
                    else:
                        next = next_any
        else:
            next = end

        if start != 0x00100000: # skip __ctr_start
            sym_map[start] = name

        if (end > next_any):
            echo (f"OVERLAP! {name} touching next symbol. {str_addr(end)} > {str_addr(next_any)}")
        elif (end > next):
            echo (f"BUG! {name} touching next symbol of same type. {str_addr(end)} > {str_addr(next)}")
        elif (start > next_any):
            echo (f"WRONG ADDR! {name} is followed by a lower address. {str_addr(start)} > {str_addr(next_any)}")
        elif (start > next):
            echo (f"WRONG ADDR! {name}\'s next same-type symbol has a lower address. {str_addr(start)} > {str_addr(next)}")

        ranges.append((start, end, name, typ, next, is_gen))

    ranges.sort(key=lambda x: x[0])
    return sym_map, ranges
