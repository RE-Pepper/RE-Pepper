#!/usr/bin/env python3
import os
import re
import sys
import bisect
import struct
import argparse
from pathlib import Path
from capstone import *
from capstone.arm import *

sys.path.append(str(Path(__file__).resolve().parent.parent))
from splector._utils import *
from tools.low.glob import getBinFile, getSplitAsmDir
from tools.low.updateMap import updateFull
from tools.low.readHeader import *

# Reads every function notes different cases, and disassembles the binary.
# Code is detected with references, where functions must already exist within a map (not detected)
# use init.py to detect functions for initial map analysis

file_sym_count_max = 111

md = None

flag_doUpdate = False
flag_useNextAddr = False
flag_ffaddr = 0

data_start = 0
data_end = 0
data_addrs = set() # defined data
data_refs_in_func = set()
addr_done = set() # defined data in functions
datablob_refs = set() # references inside current function
datablob_ext = set() # part of referenced data inside current function
data_instr_adr = set() # saves all future adr mnemonic instructions
func_refs = set() # all referenced func
func_exts = set() # externals
label_log = set() # log of labels per file
func_asm_list = set() # collection of all asm functions
ext_calls = set() # set of out of function labes for asm
switchcases = set() # jumpcases inside current function
switchtable_entry = set() # jumptable entries inside current function
switchtables = set() # all jumptable identifiers (1 = 1 jumptable)
noref_list = set() # datas that should not contain refs
data_view = [] # all data bytes of program
ranges = {} # symbol map all
ranges_data = [] # symbol map data
ranges_data_dict = {} # symbol dict data
sym_map = {} # table with symbols (addr: name)
symbols_map = {} # for final map updating
func_ends = {}
func_types = {}
data_symbol_last = 0
data_prev_tag = ""
header = None

def data_line_builder_get_sym(addr):
    myname = None
    size = 4
    if addr in ranges_data_dict:
        myname = sym_map.get(addr)
        size = ranges_data_dict[addr][1] - ranges_data_dict[addr][0]
    elif (addr in data_refs_in_func) or (addr in data_addrs) or (addr in datablob_refs):
        myname = f"dat_{addr:08X}"

    return myname, size

def data_line_build(addr, data, datatype, info, tag, sect, is_first, is_asm, is_ext):
    global label_log

    is_data = addr >= data_start
    do_export = is_data or is_asm
    myname, size = data_line_builder_get_sym(addr)

    str = ''
    if myname:
        if addr < data_start or sect == 1: # sect=1 is skip flag
            sect = None
        if not sect and tag:
            sect = typeToSection(tag, myname)
        # add directives (meta)
        str += meta_add(tag, sect, myname, size, do_export, is_data)

        # set tag for later check
        data_prev_tag = tag
        # log my label to avoid duplicate defs
        label_log.add(myname)

    # write line
    str += f"{f'    {datatype} {data}':<84}; 0x{addr:08X} "
    # add data info
    if is_first:
        str += f"({info})\n"
    else:
        str += f"\n"
    
    return str

def dump_data_single(addr, size, caller, tag, sect=None):
    global data_symbol_last

    lines = []
    
    pc = addr - header[HeadType.Text][HeadVal.Start]
    if pc < 0 or pc >= len(data_view):
        return lines
    size = min(size, len(data_view) - pc)
    offset = 0

    if addr in addr_done:
        return lines

    for ai in range(size):
        a = addr + ai
        addr_done.add(a)

    if addr > data_start:
        if addr in sym_map:
            data_symbol_last = addr
            symbols_map[data_symbol_last] = [0,tag]
        if data_symbol_last:
            symbols_map[data_symbol_last][0] += size
    
    while offset < size:
        a = addr + offset
        is_first = offset == 0
        remaining = size - offset

        if (not a in noref_list) and remaining >= 4:
            val = struct.unpack_from("<I", data_view, pc + offset)[0]
            if header[HeadType.Text][HeadVal.Start] < val < header[HeadType.Bss][HeadVal.End]:
                myline = dump_data_ref(a, caller, tag, sect, is_first)
                if myline:
                    lines.append(myline)
                    offset += 4
                    continue

        val = data_view[pc + offset]
        lines.append(data_line_build(a, f"0x{val:02X}", "DCB", "data", tag, sect, is_first, False, False))
        offset += 1
    return lines

def dump_data_ref(addr, caller, tag, sect, is_first=False): # 
    global ext_calls, func_exts

    pc = addr - header[HeadType.Text][HeadVal.Start]
    out = f";ERROR AT {addr} (ref)"
    if pc < 0 or pc >= len(data_view):
        return out

    val = struct.unpack_from("<I", data_view, pc)[0] # get 4 byte word

    if caller is None:
        is_func = False
        is_asm = False
        is_ext = False
    else:
        is_func = "f" in caller[3]
        if is_func:
            is_asm = ("a" in caller[3]) and (val in func_asm_list)
            is_ext = (val < caller[0]) or (val >= caller[4])

    ref_name = None

    str = [1, f"0x{val:08X}"] # type, data

    if is_func: # check is function
        if not is_ext or is_asm: # inside of callee function
            if val in sym_map:
                str = ["ref", sym_map.get(val)]
                ref_name = str[1]
            elif val in datablob_refs:
                str = ["data", f"dat_{val:08X}"]
                ref_name = str[1]
            elif val in switchcases:
                str = ["switch case", f"case_{val:08X}"]
            else: # just local
                str = ["local ref", f"loc_{val:08X}"]
                if val == 0x00113E9C: echo ("BRO")
                if is_asm:
                    ext_calls.add(val)
        elif (val in sym_map) and is_ext: # defined symbol
            myinfoname = "func ref" if val < data_start else "data ref"
            str = [myinfoname, sym_map.get(val)]
            ref_name = str[1]
    elif (val in sym_map): # treat as any other data ( found in preprocessing )
        str = ["data ref", sym_map.get(val)]
        ref_name = str[1]
    if header[HeadType.Bss][HeadVal.Start] <= val < header[HeadType.Bss][HeadVal.End]:
        str[0] = "bss ref"

    if str[0] == 1:
        return None
    elif RE_SPECIAL.search(str[1]):
        str[1] = f"|{str[1]}|"

    if ref_name and (not caller or is_ext):
        func_exts.add(ref_name)

    return data_line_build(addr, str[1], "DCDU", str[0], tag, sect, is_first, is_asm, is_ext)

def dump_data(f):
    start = f[0]
    size = f[1] - f[0]
    for j in range(size): # avoid writing out again
        if (start+j) in addr_done:
            return []
    lines = dump_data_single(f[0], f[1]-f[0], f, f[3], f[8])
    return lines

def disassemble_func(f):
    global md, datablob_refs, ext_calls, func_exts, label_log

    pc = f[0] - header[HeadType.Text][HeadVal.Start]
    fstart = f[0]
    if flag_useNextAddr:
        fend = f[4]
    else:
        fend = f[1]
    size = fend - fstart
    fpool = f[7]
    name = f[2]
    lines = []
    locals = set()
    datablob_list = {}

    instrs = list(md.disasm(data_view[pc:pc+size], f[0]))

    # Pass 0: Fake instruction generation and local labels
    for i_idx, i in enumerate(instrs):
        if i.id == 0: # is ignored data blob, generate fake instructions for data
            blob_start = i.address
            blob_end = i.address + i.size

            fake_instrs = []
            addr = blob_start
            while addr < blob_end:
                fake_instrs.append(FakeDataInsn(addr, data_view[addr - header[HeadType.Text][HeadVal.Start] : addr - header[HeadType.Text][HeadVal.Start] + 4]))
                addr += 4

            instrs[i_idx:i_idx+1] = fake_instrs
            continue

        if i.mnemonic.lower().startswith('b'):
            op = i.operands[0]
            if op.type == CS_OP_IMM and f[0] <= op.imm < fend:
                locals.add(op.imm)

    # Pass 1: Find data refs
    for i_idx, i in enumerate(instrs):
        if (i.bytes == b'\x00\x00\x00\x00'):
            datablob_list[i.address] = i.address
        elif i.operands:
            op_len = len(i.operands)
            for op_idx, op in enumerate(i.operands):
                if op.type == CS_OP_MEM and op.mem.base == ARM_REG_PC: # ex: add r1, pc, #0x8
                    addr = i.address + 8 + op.mem.disp
                    datablob_list[i.address] = addr

                elif op.type == CS_OP_REG and op.reg == ARM_REG_PC: # ex: ldr r1, [pc, #0x8]
                    if op_len < 2 or op_idx >= op_len-1:
                        continue

                    prev = i.operands[op_idx-1]
                    next = i.operands[op_idx+1]
                    if (prev.type != CS_OP_REG) or (prev.reg == ARM_REG_LR):
                        continue
                    if next.type != CS_OP_IMM:
                        continue
                    offset = next.imm

                    if op_len == 4:
                        last = i.operands[op_idx+2]
                        if last.type != CS_OP_IMM:
                            echo (f"Got weird ref at {str_addr(i.address)}: 4 ops but last not imm")

                        if offset != 0:
                            rot = last.imm
                            ((next.imm >> rot) | (next.imm << (32 - rot))) & 0xFFFFFFFF
                        else:
                            echo ("bruh")

                    elif op_len > 4:
                        echo (f"Got weird ref at {str_addr(i.address)}: more than 4 ops")
                        
                    data_instr_adr.add(i.address)
                    if "sub" in i.mnemonic.lower():
                        addr = i.address + 8 - offset
                    else:
                        addr = i.address + 8 + offset
                    datablob_list[i.address] = addr

    # Pass 2: Jumptables
    for i_idx, i in enumerate(instrs):
        if i.mnemonic.lower() == "ldrlo": # found jump table / switch case
            datablob_list.pop(i.address, None)
            next_idx = i_idx+1
            attempts = 4
            while next_idx < len(instrs):
                nexti = instrs[next_idx]
                attempts -= 1
                val = struct.unpack_from("<I", data_view, nexti.address - header[HeadType.Text][HeadVal.Start])[0]
                if not (fstart <= val < fend): # val is not a case
                    if attempts <= 0:
                        next_idx = len(instrs)
                    else:
                        next_idx += 1
                    continue
                # if here, we got a case.
                attempts = 0
                locals.add(val)
                data_addrs.add(nexti.address)
                datablob_list.pop(nexti.address, None)
                switchcases.add(val)
                switchtable_entry.add(nexti.address)
                next_idx += 1

                if not (i.address in switchtables) and ((nexti.address == fpool) or (val > fpool)):
                    echo (f"DATA ADDR WRONG! Function {f[2]} at {str_addr(fstart)} has data address in jump table.")
                switchtables.add(i.address)
            continue

    datablob_set = set(v for v in datablob_list.values() if v is not None)
    # Pass 3: Bigger Data scan
    for i_idx, i in enumerate(instrs):
        not_pool = not fpool or (i.address < fpool)
        if not_pool:
            if i_idx == 0 or not (i.address in data_addrs or i.address in datablob_set):
                continue
            # this is ref. data
        if i.address in switchtable_entry: # skip jtables
            continue

        # add and ref data here
        if i.address in datablob_set or i.address == fpool:
            data_refs_in_func.add(i.address)

        if not_pool:
            # find a possible local branch or function end, only first data
            prev = instrs[i_idx-1]
            mnem = prev.mnemonic.lower()
            if not mnem in ("b", "bx", "pop", "bl") and (i.bytes != b'\x0e\xf0\xa0\xe1'):
                continue

        for try_addr in range(i.address, fend, 4): # from now to function end
            if try_addr in locals: # detected branch, was blob inside function
                break
            if try_addr >= fend: # function end, was blob after function
                break

            if not try_addr in datablob_ext:
                datablob_ext.add(try_addr)

    datablob_refs.clear()
    # Pass 4: Remove wrong data references
    for ia, addr in datablob_list.items():
        if addr is None:
            continue
        if ia in datablob_ext and not addr in datablob_ext:
            data_refs_in_func.discard(addr)
            continue
        if (addr < fstart or addr >= fend) and not ("a" in f[3] and addr in func_asm_list):
            error_func(f, instrs, f"Reference at 0x{ia:08X} to 0x{addr:08X} is out of function bounds!")

        datablob_refs.add(addr)
    for a in datablob_ext:
        datablob_refs.add(a)
    for ia, addr in list(datablob_list.items()):
        if addr not in datablob_refs:
            del datablob_list[ia]

    has_instr = False
    lp_start = 0
    # Pass 5: Writing the lines
    for i_idx, i in enumerate(instrs):
        if i.address in addr_done:
            continue
        # check if current instr is actually data
        if (i.address in data_addrs) or (i.address in datablob_refs) or (i.address > fend) or (".word" in i.mnemonic.lower()):
            mydatasize = 4 # find size if possible, else 4
            if i.address in sym_map:
                for sym in ranges_data:
                    if sym[0] != i.address:
                        continue

                    func_exts.add(sym[2]) # add external
                    if sym[1] and sym[1] > sym[0]:
                        mydatasize = sym[1] - sym[0]
                    break

            lines_data = dump_data_single(i.address, mydatasize, f, None, f[8])
            for line in lines_data:
                lines.append(line) # dump em

            for x in range(mydatasize): # notify data not to write again
                addr_done.add(i.address + x)
            if ".word" in i.mnemonic.lower() and (i.address not in data_addrs) and (i.address not in datablob_refs) and (i.address <= fend):
                echo (f"Info: resolved leftover .word at 0x{i.address:08X}")
            if flag_doUpdate and lp_start == 0:
                lp_start = i.address
            continue

        # this is an instruction.
        has_instr = True
        for ai in range(4): # mark every byte as done
            addr_done.add(i.address + ai)

        op_str = i.op_str
        op_len = len(i.operands)
        target = None
        mnemonic = i.mnemonic
        extrainfo = ""

        # replace labels
        if i.address in datablob_list:
            target = datablob_list.get(i.address) # pc relative (data pools)
        elif any(p in i.mnemonic for p in ("ldr", "str", "b", "adr")):
            for op_idx, op in enumerate(i.operands):
                if op.type == CS_OP_IMM: # direct reference
                    target = op.imm

        if target and (target > header[HeadType.Text][HeadVal.Start] and target < data_end):
            is_ext = target < fstart or target >= fend
            is_asm = "a" in f[3] and target in func_asm_list

            labelname = None # target in data_addrs, target < data_start
            if target in sym_map and (target in data_addrs) != (target < data_start): # known
                labelname = sym_map.get(target)
                if target != f[0]:
                    func_exts.add(labelname) # add external
            elif target in datablob_refs: # is local data
                labelname = f"dat_{target:08X}"
                #if is_ext:
                #    func_exts.add(labelname)
            elif not is_ext or is_asm: # is local code
                if target in switchcases:
                    labelname = f"case_{target:08X}"
                else:
                    labelname = f"loc_{target:08X}"
                    if is_ext and is_asm:
                        extrainfo += " (external asm branch)"
                        ext_calls.add(target)
                        func_exts.add(labelname)

            if (labelname is None):
                if (target % 4096 != 0): echo (f"Warn: Failed to resolve label from {f[2]} : 0x{i.address:08X} to 0x{target:08X}")
            else:
                if target in datablob_refs:
                    if i.address in data_instr_adr: mnemonic = "adr"
                    op_str = re.sub(r'\[?\bpc\b(,[- ]?#?-?(0x)?[0-9a-fA-F]+(, #?(0x)?[0-9a-fA-F]+)?)?\]?', labelname, op_str)
                elif op.type == CS_OP_IMM:
                    op_str = re.sub(r'#?0x[0-9a-fA-F]+', labelname, op_str)

        # write directives
        label = ''

        if i.address == fstart:
            mytype = f[3]
            myname = f[2]
            if f[8]:
                mytype = func_types.get(f[8])
                if f[8] == header[HeadType.Text][HeadVal.Start]:
                    myname = "__ctr_start"
                else:
                    myname = sym_map.get(f[8])
            label += meta_add("f", typeToSection(mytype, myname), f[2], f[1] - f[0], True, True)
            extrainfo += " (asm function)"

        elif (i.address in locals) or (i.address in ext_calls):

            if i.address in switchcases:
                my_labelname = f"case_{i.address:08X}"
            else:
                my_labelname = f"loc_{i.address:08X}"
            label += f"\n{my_labelname}\n"
            label_log.add(my_labelname)

        # write final instruction line
        bytes_hex = ''.join(f'{b:02X}' for b in i.bytes)
        lines.append(label + f"    {mnemonic.upper():<8} {op_str:<70} ; 0x{i.address:08X} - {bytes_hex}{extrainfo}\n")

    if has_instr == False:
        error_func (f, instrs, f"No instructions!")

    lines.append("    ENDFUNC\n\n")

    if flag_doUpdate and lp_start:
        # overwrite function end
        func_ends[fstart] = lp_start

    return lines

def disassemble_symbol(f):
    global func_exts,  datablob_refs, datablob_ext, switchcases, switchcases_entry

    if f[0] in addr_done:
        return []  # already written

    if not "f" in f[3]:
        return dump_data(f)

    lines = disassemble_func(f)
    if not lines: # not a valid function after all
        return dump_data(f)

    # valid function
    blob = sorted(datablob_refs)
    for idx, d in enumerate(blob):
        if d in addr_done:
            continue  # already written
        if (d >= f[4] or d < f[0]) and not ("a" in f[3] and d in func_asm_list):
            echo (f"Warn: Attempted to add data addr {str_ddr(d)} to {f[2]} ({str_addr(f[0])}), which is out of its bounds.")
            continue
        if idx == len(blob) - 1:
            size = f[4] - d
        else:
            size = blob[idx+1] - d
        lines_data = dump_data_single(d, size, f, None, None)
        for line in lines_data:
            lines.append(line)
    datablob_refs.clear()
    datablob_ext.clear()
    switchcases.clear()
    switchtable_entry.clear()

    return lines

def assemble_data(addr):
    global label_log

    size = 4
    do_refs = True
    tag = None
    sect = None
    lines = []

    # get size
    sym_found = False
    if addr in sym_map:
        size = 0
        for sym in ranges_data:
            if addr == sym[0]:
                sym_found = True
                label_log.add(sym[2])
                if sym[3] == "db": # skip bss
                    return []
                tag = sym[3]
                if sym[1] and sym[1] > addr:
                    size = sym[1] - addr # if end addr, get correct size
                break

        if size == 0:
            nextadr = min((a for a in sym_map if a > addr), default=data_end)
            size = nextadr - addr # get next start address in map

    if not (flag_doUpdate or sym_found):
        return [] # avoid writing unknown bytes if not updating map

    if sym_found and not tag:
        sym_idx = bisect.bisect_left(ranges_data, addr, key=lambda x: x[0])
        if sym_idx > 0:
            up = ranges_data[sym_idx - 1]
        if sym_idx < len(ranges_data):
            down = ranges_data[sym_idx + 1]

        # decide which to use
        if up and down: # get closest
            ddown = addr - down[0]
            dup = up[1] - addr

            if dup == ddown:
                tag = down[3]
            elif ddown > dup:
                tag = up[3]
            else:
                tag = down[3]
        elif up:
            tag = up[3]
        elif down:
            tag = down[3]
        else:
            tag = "d" # fallback

        # strip per-symbol properties
        tag = tag.replace("r", "").replace("g", "")

    if (addr % 4) != 0:
        sect = 1 # append unaligned ones to prev

    lines_data = dump_data_single(addr, size, None, tag, sect)
    for line in lines_data:
        lines.append(line)

    return lines

def run(do_update=None):
    global md, data_view, data_start, data_end, sym_map, ranges, noref_list, flag_doUpdate, flag_ffaddr, func_types, header, label_log
    
    if not do_update is None:
        flag_doUpdate = do_update
    if flag_ffaddr is None:
        flag_ffaddr = 0

    upd_status ("Loading map")
    sym_map, ranges = load_map()

    count_lines = 0
    count_syms = 0
    count_files = 0

    file_name = None
    file_sym_count = 0

    lines_file = []
    first_addr_in_file = None

    upd_status("Preparing")
    with open(getBinFile(), 'rb') as f:
        data = f.read()
    data_view = memoryview(data)

    header = read_header()

    md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
    md.detail = True
    md.skipdata = True

    if flag_ffaddr == 0:
        if os.path.exists(getSplitAsmDir()):
            echor ("Output exists, deleting....")
            shutil.rmtree(getSplitAsmDir())
            echo ("Output exists, deleted.")
        getSplitAsmDir().mkdir(parents=True, exist_ok=True)

    upd_status("Preprocessing")
    for a, f in ranges.items(): # find all data symbols
        if "r" in f[3]: # noref specified
            for a in range(f[0], f[4], 1):
                noref_list.add(a)
        if "a" in f[3]: # asm
            for a in range(f[0], f[4], 1):
                func_asm_list.add(a)
        if "d" in f[3]:
            size = f[1] - f[0]
            data_addrs.add(f[0])
        else:
            data_start = f[1]
            func_types[f[0]] = f[3]
    data_end = len(data_view) + header[HeadType.Text][HeadVal.Start]

    
    if flag_doUpdate:
        # try find references
        endaddr = header[HeadType.Text][HeadVal.Start] + len(data_view)
        for off in range(0, len(data_view), 4):
            if (off + header[HeadType.Text][HeadVal.Start]) in noref_list:
                continue
            val = struct.unpack_from("<I", data_view, off)[0]
            if (header[HeadType.Text][HeadVal.Start] < val < endaddr) and (val not in sym_map):
                if val > data_start:
                    sym_map[val] = f"dat_{val:08X}"

    upd_status("Splecting and writing assembly")

    # Start writing data
    set_status ("Splecting func ")

    # extra data ranges
    for a, sym in ranges.items():
        if "d" in sym[3]:
            ranges_data.append(sym)
            ranges_data_dict[sym[0]] = sym

    def write_asm_file(override_name=None, silent=False, sort=True):
        global label_log, func_exts
        nonlocal count_files, lines_file, file_sym_count, file_name
        file_name = ""
        if override_name:
            file_name = get_file(override_name)
        else:
            file_name = get_asm_file(first_addr_in_file)

        file_sym_count = 0
        if not silent:
            count_files += 1
        with open(file_name, 'w', newline='\r\n', encoding='utf-8') as out:
            # write imports
            if len(func_exts) > 0:
                imports = sorted(func_exts) if sort else func_exts
                for e in sorted(func_exts):
                    if not e in label_log:
                        my_e = f"|{e}|" if RE_SPECIAL.search(e) else e
                        out.write(f"    IMPORT {my_e}\n")
                        label_log.add(e)
            out.write("\n    PRESERVE8\n")
            
            # write data
            out.writelines(lines_file)
            out.write("\n    END\n")
        lines_file.clear()
        label_log.clear()
        func_exts.clear()

    # Write out functions
    ranges_list = list(ranges.values())
    for i, f in enumerate(ranges_list):
        if f[0] >= data_start:
            continue
        if f[0] < flag_ffaddr:
            set_progress (f"FF 0x{f[0]:08X}")
            continue
        set_progress (f"0x{f[0]:08X}")
        print_progress()

        lines = disassemble_symbol(f)

        if len(lines) <= 0:
            continue

        if file_sym_count == 0:
            first_addr_in_file = f[0]

        label_log.add(f[2])
        count_lines += len(lines)
        count_syms += 1
        file_sym_count += 1

        lines_file.extend(lines)

        is_next_mine = (i != len(ranges_list)-1) and f[8] and (ranges_list[i+1][8] in (f[8], f[0]))
        is_this_reset = (file_sym_count > file_sym_count_max) and not is_next_mine
        if is_this_reset:
            write_asm_file()

        error_exec()

    if not first_addr_in_file:
        fail ("Nothing to split was found, cannot be.")

    write_asm_file()

    set_status ("Splecting data ")

    # Write out data
    if flag_doUpdate:
        my_datalist = range(data_start, data_end, 1)
    else:
        my_datalist = [r[0] for r in ranges_data]
    for addr in my_datalist:
        if addr in addr_done:
            continue
        if addr < flag_ffaddr:
            set_progress (f"FF 0x{addr:08X}")
            continue
        set_progress (f"0x{addr:08X}")
        print_progress()

        lines = assemble_data(addr)

        if len(lines) <= 0:
            continue

        if file_sym_count == 0:
            first_addr_in_file = addr

        count_lines += len(lines)
        count_syms += 1
        file_sym_count += 1

        lines_file.extend(lines)

        is_this_reset = (file_sym_count > file_sym_count_max)

        if is_this_reset:
            write_asm_file()

    write_asm_file()

    if flag_ffaddr != 0:
        echo (f"SPLIT INCOMPLETE, STARTED FROM {flag_ffaddr}")
    echo (f"Wrote {count_syms} symbols among {count_lines} lines in {count_files} files")


    if flag_doUpdate:
        set_status("Updating map")
        set_progress("")
        print_progress()

        # start, end, name, typ, next, is_gen, rank
        # go through every known data
        for addr, data in symbols_map.items():
            start = addr
            end = addr + data[0]
            if addr in ranges:  # symbol exists, but update
                sym = ranges[addr]
                sym[1] = end # set end to new end
                sym[4] = end # set next to new end
                ranges[addr] = sym
            else:  # new, add
                ranges[start] = [start, end, "", data[1], end, True, "U", end]

        # update all symbols
        for a, sym in ranges.items():
            if (sym[5]):  # is autogenerated
                sym[2] = ""
            if (sym[0] in func_ends): # reassign function ends
                sym[7] = func_ends.get(sym[0])

        # Convert to map syms
        sym_list = [sym_conv(sym) for a, sym in ranges.items()]

        # Sort
        sym_list.sort(key=lambda x: x[MapFmt.Start])  # sort it

        updateFull(sym_list)

    func_exts.update(list(map(sym_map)))
    write_asm_file("depend.s", True, False)

    set_status("Splectoratic!")
    set_progress("")
    print_progress()

if "split.py" in sys.argv[0]:
    parser = argparse.ArgumentParser('split.py', description="Splector 5000")
    parser.add_argument('-u', action='store_true', help="Attempt to update map (dangerous!)")
    parser.add_argument('-a', action='store_true', help="Use next symbol start for function end instead of defined end")
    parser.add_argument('-q', action='store_true', help="Do not print progress")
    parser.add_argument("ffaddr", nargs="?", type=lambda x: int(x, 0), default=None, help="Skip until addr (avoids cleaning)")
    args = parser.parse_args()
    sys.argv = [sys.argv[0]] # clear args

    flag_doUpdate = args.u
    flag_useNextAddr = args.a
    flag_ffaddr = args.ffaddr

    set_silent(args.q)
    run()

