#!/usr/bin/env python3
import os
import re
import sys
import shutil
from enum import IntEnum
from pathlib import Path
from capstone import *

sys.path.append(str(Path(__file__).resolve().parent.parent))
from tools.low.__readMap import *
from tools.low.__utilsElf import typeToSection

curname = ""
curstatus = "Initializing"

meta_lastsect = "wopee" # last sect
meta_sect = "wopee" # curr sect

is_silent = False

RE_SPECIAL = re.compile(r'[^a-zA-Z0-9_]')

def set_silent(state):
    global is_silent
    is_silent = state
    if is_silent:
        echo ("Not printing progress.")

def set_progress(name):
    global curname
    curname = name
def set_status(status):
    global curstatus
    curstatus = status

def clear_line():
    if is_silent: return
    print (' ' * shutil.get_terminal_size((80, 20)).columns, end='\r')
def print_progress():
    if is_silent: return
    clear_line()
    print ("\033[38;5;172m" + curstatus + "\033[38;2;150;75;0m" + curname + "\033[0m\033[K ...", end='\r')

def upd_status(status):
    if is_silent: return
    set_status(status)
    print_progress()

def echor(str, end="\r"):
    print (f"\033[38;5;221m{str}\033[0m\033[K", end=end)
def echo(str, end="\n"):
    clear_line()
    echor(str, end)

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
                sym[t] = map_sym[2]

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

def clean_dir(out_dir):
    if os.path.exists(out_dir):
        echor ("Output exists, deleting....")
        shutil.rmtree(out_dir)
        echo ("Output exists, deleted.")
    os.makedirs(out_dir, exist_ok=True)

def get_file(name):
    return str(getSplitPath() / name)
def get_asm_file(addr):
    return str(getSplitPath() / f"a{addr:08X}.s")

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
    return name, False

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

def typeToSectionAttr(type):
    if not type:
        return None
    elif "f" in type:
        return "CODE,READONLY"
    elif "d" in type and not "c" in type:
        return "DATA,READWRITE"
    else:
        return "DATA,READONLY"

def meta_add(type_code, sect, name, size, do_export=False, do_meta_ext=False):
    global meta_lastsect, meta_sect

    type = typeToSectionAttr(type_code)

    if sect:
        meta_sect = sect if meta_lastsect != sect else None
        meta_lastsect = sect

    if RE_SPECIAL.search(name):
        name = f"|{name}|"

    line = '\n'
    if do_export:
        if meta_sect and type:
            line += f"    AREA |{meta_sect}|,{type}\n"
        else:
            line += "\n"
        line += f"    EXPORT {name}"
        if do_meta_ext:
            line += f" [WEAK,SIZE=0x{size:X}]\n"
        else:
            line += "\n"

    line += f"{name}"
    if type and "CODE" in type:
        line += " FUNCTION"
    line += "\n"

    return line

def load_map():
    sym_map = {}
    ranges = {}
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

        if "b" in typ:
            continue

        name, is_gen = check_name(sym[MapFmt.Symbol], typ, start) # valid name

        if i < (symlen-1):
            next_any = syms[i+1][MapFmt.Start]
        else:
            next_any = end

        if end is None or end <= start:
            if symlen == i+1:
                fail ("Last symbol has no end.")
            elif not "d" in typ and symlen > (i+1):
                end = next_any

        if i < (symlen-1):
            if "d" in typ:
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
        #elif (start % 4) != 0:
        #    echo (f"BAD ADDR! {str_addr(start)} is not 4 byte aligned!")
        #elif (name in sym_map):
        #    echo (f"DUPLICATE NAME! {name} is used for more than one symbols!")

        if start != 0x00100000: # skip __ctr_start
            sym_map[start] = name

        ranges[start] = ((start, end, name, typ, next, is_gen, rank, pool, section))

    return sym_map, ranges
