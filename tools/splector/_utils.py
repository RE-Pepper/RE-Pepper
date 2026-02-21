#!/usr/bin/env python3
import os
import sys
import shutil
import pathlib
from enum import IntEnum
from colorama import Fore, Style
from capstone import *

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))
from low.__parseMap import *
from low.__utilsElf import typeToSection

curname = ""
curstatus = "Initializing"

meta_lastfunc = None # curr/last func
meta_lastfunc_do_size = False
meta_lastdata = None # last data that had meta (.global .type .size) written
meta_lastdata_do_size = False

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
    return f"0x{a:08X}"
def str_addrs(addrs):
    return (", ".join(str_addr(a) for a in addrs))
def str_instr(i):
    return f"0x{i.address:08X}: {i.mnemonic} {i.op_str}"
def str_instrs(instrs):
    return ("\n".join(str_instr(i) for i in instrs))
def str_func(f):
    pool = f"-0x{f[7]:08X}" if f[7] else ""
    return f"0x{f[0]:08X}{pool}-0x{f[1]:08X}: {f[2]} ({str(f[3])}) > 0x{f[4]:08X} ? {f[5]}"
def str_sym(f):
    return f"0x{f[MapFmt.Start]:08X}-0x{f[MapFmt.End]:08X}: {f[MapFmt.Symbol]} ({str(f[MapFmt.Type])}, {f[MapFmt.Rank]})"

def sym_conv(map_sym):
    sym = [None] * len(MapFmt)
    for col in MapFmt:
        match col:
            case MapFmt.Start as t:
                sym[t] = map_sym[0]
            case MapFmt.End as t:
                sym[t] = map_sym[1] # prefer next
            case MapFmt.Pool as t:
                sym[t] = map_sym[7] if (map_sym[7] != map_sym[1]) else None
            case MapFmt.Rank as t:
                sym[t] = map_sym[6] if map_sym[6] else "U"
            case MapFmt.Type as t:
                sym[t] = map_sym[3]
            case MapFmt.Symbol as t:
                sym[t] = map_sym[2].replace("$$_$$", "::")

    return sym

error_list = []
error_details = ""
def error_func(f, instrs, str):
    global error_details
    error_list.append(f"ERROR! Function at 0x{f[0]:08X} : {str}")
    if error_details != "":
        return
    line=[]
    line.append(f"Details: Range: 0x{f[0]:08X} - 0x{f[1]:08X}, Name: {f[2]}, Next Func Start: 0x{f[4]:08X}")
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

def fail(msg: str):
    echo (msg)
    sys.exit(1)

def check_name(name, typ, addr):
    if not name or name.strip() == "":
        if (typ == "f"):
            return f"fn_{addr:08X}", True
        elif (typ is None or typ == ""):
            return f"unk_{addr:08X}", True
        else:
            return f"dat_{addr:08X}", True
    return name.replace("::", "$$_$$"), False

class FakeDataInsn:
    __slots__ = ("address", "size", "id", "mnemonic", "op_str", "operands", "bytes")

    def __init__(self, addr, raw_bytes):
        self.address = addr
        self.size = 4
        self.id = 0
        self.mnemonic = ".word"
        self.op_str = ""
        self.operands = []
        self.bytes = bytes(raw_bytes)

    def __repr__(self):
        attrs = ", ".join(f"{k}={getattr(self, k)!r}" for k in self.__slots__)
        return f"<FakeDataInsn {attrs}>"

def meta_add_start(name, is_func=False, do_size=False):
    global meta_lastdata, meta_lastfunc, meta_lastfunc_do_size, meta_lastdata_do_size

    line = ''

    if is_func: # next function begins
        if meta_lastfunc and meta_lastfunc_do_size:
            line += f".size {meta_lastfunc}, .-{meta_lastfunc}\n"
            meta_lastfunc = None
        meta_lastfunc = name
        meta_lastfunc_do_size = do_size
    else:
        if meta_lastdata and meta_lastdata_do_size:
            line += f".size {meta_lastdata}, .-{meta_lastdata}\n"
            meta_lastdata = None
        meta_lastdata = name
        meta_lastdata_do_size = do_size

    return line

def typeToSectionAttr(type):
    if not type:
        return "a"
    elif "f" in type:
        return "ax"
    elif "d" in type and not "c" in type:
        return "aw"
    else:
        return "a"

def meta_add(objtype, sectname, name, do_export=False):
    line = ''
    if do_export:
        line += f"\n.global {name}"
    if objtype:
        line += f"\n.weak {name}"
        line += f"\n.type {name} %{objtype}"
        if sectname:
            line += f"\n.section {sectname},\"{typeToSectionAttr(objtype)}\",%progbits"
    line += f"\n{name}:\n"

    return line
def meta_add_data(objtype, sectname, do_export=False):
    return meta_add(objtype, sectname, meta_lastdata, do_export)
def meta_add_func(objtype, sectname):
    return meta_add(objtype, sectname, meta_lastfunc, True)

def load_map():
    sym_map = {}
    ranges = []
    syms = read_sym_file()
    symlen = len(syms)
    for i in range(symlen):
        sym = syms[i]
        start = sym[MapFmt.Start]
        end = sym[MapFmt.End]
        typ = sym[MapFmt.Type]
        rank = sym[MapFmt.Rank]
        pool = sym[MapFmt.Pool]
        section = sym[MapFmt.Section]
        is_data = "d" in sym[MapFmt.Type]

        name, is_gen = check_name(sym[MapFmt.Symbol], typ, start) # valid name

        if i < (symlen-1):
            next_any = syms[i+1][MapFmt.Start]
        else:
            next_any = end

        if end is None or end <= start:
            if symlen == i+1:
                fail ("Last symbol has no end.")
            elif not is_data and symlen > (i+1):
                end = next_any

        if i < (symlen-1):
            if is_data:
                next = next_any
            else:
                next = 0
                if "f" in syms[i+1][MapFmt.Type]:
                    next = next_any
                else:
                    for s in syms[i+1:]:
                        if "f" in s[MapFmt.Type]:
                            next = s[MapFmt.Start]
                            break
                if next == 0:
                    if end <= start:
                        next = next_any
                    else:
                        next = end
        else:
            next = end

        if (end > next_any):
            echo (f"OVERLAP! {name} touching next symbol. {str_addr(end)} > {str_addr(next_any)}")
        elif (end > next):
            echo (f"BUG! {name} touching next symbol of same type. {str_addr(end)} > {str_addr(next)}")
        elif (start > next_any):
            echo (f"WRONG ADDR! {name} is followed by a lower address. {str_addr(start)} > {str_addr(next_any)}")
        elif (start > next):
            echo (f"WRONG ADDR! {name}\'s next same-type symbol has a lower address. {str_addr(start)} > {str_addr(next)}")
        elif (start in sym_map):
            echo (f"DUPLICATE ADDR! {std_addr(start)} is the start address in more than 2 symbols!")
        elif (name in sym_map):
            echo (f"DUPLICATE NAME! {name} is used for more than one symbols!")

        if start != 0x00100000: # skip __ctr_start
            sym_map[start] = name

        ranges.append((start, end, name, typ, next, is_gen, rank, pool, section))

    ranges.sort(key=lambda x: x[0])
    return sym_map, ranges
