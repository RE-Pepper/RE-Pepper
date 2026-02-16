import csv
import os
import re
import sys
import shutil
import struct
from capstone import *
from capstone.arm import *
from _settings import *
from splector._utils import *
from low.__updateMap import updateFull

md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
md.detail = True
md.skipdata = True

BASE_ADDR = 0x00100000
data_start = 0
data_end = 0
data_addrs = set() # defined data
data_refs_in_func = set()
addr_done = set() # defined data in functions
datablob_refs = set() # references inside current function
datablob_ext = set() # part of referenced data inside current function
func_refs = set() # all referenced func
switchcases = set() # jumpcases inside current function
switchtable = set() # jumptables inside current function
noref_list = set() # datas that should not contain refs
data_view = [] # all data bytes of program
ranges = [] # symbol map all
ranges_data = [] # symbol map data
sym_map = {} # table with symbols (addr: name)
data_symbols_map = {} # for final map updating
data_symbol_last = 0

def data_line_build(addr, data, type, info, sect, is_first):
    str = ''
    if addr in data_refs_in_func:
        str += meta_add_start_addr(addr, False, False)
        str += meta_add_data(None, sect)
    elif addr in sym_map:
        str += meta_add_start(sym_map.get(addr), False, addr > data_start)
        str += meta_add_data("object" if addr > data_start else None, sect)

    str += f"{f'    .{type} {data}':<84}@ 0x{addr:08X} "
    if is_first:
        str += f"({info})\n"
    else:
        str += f"\n"
    return str

def dump_data_single(addr, size, caller, sect):
    global data_symbol_last

    lines = []
    
    pc = addr - BASE_ADDR
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
            data_symbols_map[data_symbol_last] = [0,sect]
        if data_symbol_last:
            data_symbols_map[data_symbol_last][0] += size

    alignernum = 0
    while offset < size:
        a = addr + offset
        is_first = offset == 0
        remaining = size - offset

        if (not a in noref_list) and remaining >= 4 and alignernum == 0:
            val = struct.unpack_from("<I", data_view, pc + offset)[0]
            if BASE_ADDR < val < (len(data_view)+BASE_ADDR):
                lines.append(dump_data_ref(a, caller, sect, is_first))
                offset += 4
                continue
            else:
                alignernum = 4

        val = data_view[pc + offset]
        lines.append(data_line_build(a, f"0x{val:02X}", "byte", "data", sect, is_first))
        offset += 1
        if alignernum > 0:
            alignernum -= 1
    return lines

def dump_data_ref(addr, caller, sect, is_first=False): # 
    pc = addr - BASE_ADDR
    is_func = (not caller is None) and caller[3].startswith("f")
    out = f"@ERROR AT {addr} (ref)"
    if pc < 0 or pc >= len(data_view):
        return out

    val = struct.unpack_from("<I", data_view, pc)[0] # get 4 byte word

    str = ["data ref", f"0x{val:08X}"] # type, data

    if is_func: # check is function
        if caller[0] < val < caller[1]: # inside of callee function
            if val in sym_map:
                str = ["ref", sym_map.get(val)]
            if val in datablob_refs:
                str = ["data", f"dat_{val:08X}"]
            elif val in switchcases:
                str = ["switch case", f"case_{val:08X}"]
            else: # just local
                str = ["local ref", f"loc_{val:08X}"]
        elif (val in sym_map) and (caller[1] < val >= caller[4]): # defined symbol
            str = ["func ref" if val < data_start else "data ref", sym_map.get(val)]
    elif (val in sym_map): # treat as any other data ( found in preprocessing )
        str = ["data ref", sym_map.get(val)]

    return data_line_build(addr, str[1], "word", str[0], sect, is_first)

def dump_data(f):
    start = f[0]
    size = f[1] - f[0]
    for j in range(size): # avoid writing out again
        if (start+j) in addr_done:
            return []
    lines = dump_data_single(f[0], f[1]-f[0], f, f[3])
    return lines
    

def disassemble_func(f):
    global md, datablob_refs

    pc = f[0] - BASE_ADDR
    size = f[4] - f[0]
    name = f[2]
    lines = []
    externs = set()
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
                fake_instrs.append(FakeDataInsn(addr, data_view[addr - BASE_ADDR : addr - BASE_ADDR + 4]))
                addr += 4

            instrs[i_idx:i_idx+1] = fake_instrs
            continue

        if i.mnemonic.lower().startswith('b'):
            op = i.operands[0]
            if op.type == CS_OP_IMM and f[0] <= op.imm < f[1]:
                locals.add(op.imm)

    # Pass 1: Find data refs
    for i_idx, i in enumerate(instrs):
        if i.bytes == b'\x00\x00\x00\x00':
            datablob_list[i.address] = i.address
        elif i.operands:
            for op_idx, op in enumerate(i.operands):
                if (op.type == CS_OP_MEM or op.type == ARM_OP_MEM) and op.mem.base == ARM_REG_PC: # ex: add r1, pc, #0x8
                    addr = i.address + 8 + op.mem.disp
                    datablob_list[i.address] = addr

                elif op.type == CS_OP_REG and op.reg == ARM_REG_PC: # ex: ldr r1, [pc, #0x8]
                    if len(i.operands) < 3 or op_idx >= len(i.operands)-1:
                        continue
                    prev = i.operands[op_idx-1]
                    next = i.operands[op_idx+1]
                    if (prev.type != CS_OP_REG) or (prev.reg == ARM_REG_LR):
                        continue
                    if next.type != CS_OP_IMM:
                        continue
                    if i.mnemonic.lower().startswith("sub"):
                        addr = i.address + 8 - next.imm
                    else:
                        addr = i.address + 8 + next.imm
                    datablob_list[i.address] = addr

    # Pass 2: Jumptables
    for i_idx, i in enumerate(instrs):
        if i.mnemonic.lower() == "ldrlo": # found jump table / switch case
            datablob_list[i.address] = None
            next_idx = i_idx+1
            attempts = 4
            while next_idx < len(instrs):
                nexti = instrs[next_idx]
                attempts -= 1
                val = struct.unpack_from("<I", data_view, nexti.address - BASE_ADDR)[0]
                if not (f[0] <= val < f[1]): # val is not a case
                    if attempts <= 0:
                        next_idx = len(instrs)
                    else:
                        next_idx += 1
                    continue
                # if here, we got a case.
                attempts = 0
                locals.add(val)
                data_addrs.add(nexti.address)
                datablob_list[nexti.address] = None
                switchcases.add(val)
                switchtable.add(nexti.address)
                next_idx += 1
            continue

    datablob_set = set(v for v in datablob_list.values() if v is not None)
    # Pass 3: Bigger Data scan
    for i_idx, i in enumerate(instrs):
        if i_idx == 0 or not ((i.address in data_addrs) or (i.address in datablob_set)):
            continue
        # this is ref. data
        if i.address in switchtable: # skip jtables
            continue
        # add and ref data here
        if i.address in datablob_set:
            data_refs_in_func.add(i.address)

        # find a possible local branch or function end, only first data
        prev = instrs[i_idx-1]
        mnem = prev.mnemonic.lower()
        if not mnem in ("b", "bx", "pop", "bl"):
            continue

        for try_addr in range(i.address, f[4], 4): # from now to function end
            if try_addr in locals: # detected branch, was blob inside function
                break
            if try_addr >= f[4]: # function end, was blob after function
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
        if f[5] and (addr < f[0] or addr >= f[4]):
            error_func(f, instrs, f"Reference at 0x{ia:08X} to 0x{addr:08X} is out of function bounds!")

        datablob_refs.add(addr)
    for a in datablob_ext:
        datablob_refs.add(a)

    data_addrs_sort = sorted(data_addrs)
    has_instr = False
    # Pass 5: Writing the lines
    for i_idx, i in enumerate(instrs):
        if i.address in addr_done:
            continue
        # check if current instr is actually data
        if (i.address in data_addrs) or (i.address in datablob_refs) or (i.address > f[1]) or (i.mnemonic.lower().startswith(".word")):
            mydatasize = 4 # find size if possible, else 4
            if i.address in sym_map:
                for sym in ranges_data:
                    if sym != i.address:
                        continue

                    if sym[1] and sym[1] > sym[0]:
                        mydatasize = sym[1] - sym[0]
                    break

            for line in dump_data_single(i.address, mydatasize, f, None):
                lines.append(line) # dump em

            for x in range(mydatasize): # notify data not to write again
                addr_done.add(i.address)
            if i.mnemonic.lower().startswith(".word") and (i.address not in data_addrs) and (i.address not in datablob_refs) and (i.address <= f[1]):
                echo (f"Info: resolved leftover .word at 0x{i.address:08X}")
            continue

        # this is an instruction.
        has_instr = True
        for ai in range(4): # mark every byte as done
            addr_done.add(i.address + ai)

        # replace label refs
        op_str = i.op_str
        op_len = len(i.operands)
        for op_idx, op in enumerate(i.operands):
            if op.type == CS_OP_IMM:
                target = op.imm
                is_local = f[0] < target < f[1]
                labelname = None
                if target in datablob_refs: # is local data
                    if target in sym_map:
                        labelname = sym_map.get(target)
                    else:
                        labelname = f"dat_{target:08X}"
                elif is_local: # is local code
                    if target in switchcases:
                        labelname = f"case_{target:08X}"
                    else:
                        labelname = f"loc_{target:08X}"
                elif target < data_start: # anything but data
                    labelname = sym_map.get(target)
                if labelname is None:
                    continue
                if not is_local:
                    externs.add(labelname)
                op_str = re.sub(r'#?0x[0-9a-fA-F]+', labelname, op_str)

        # write directives

        label = ''

        if i.address == f[0]:
            label += meta_add_start(f[2], True, True)

            if len(externs) > 0:
                label += "\n"
            for e in externs:
                label += f".extern {e}\n"

            label += meta_add_func("function", f[3] if f[0] != BASE_ADDR else None)

        elif i.address in locals:
            if i.address in switchcases:
                label += f"\ncase_{i.address:08X}:\n"
            else:
                label += f"\nloc_{i.address:08X}:\n"

        # write final instruction line
        bytes_hex = ''.join(f'{b:02X}' for b in i.bytes)
        lines.append(label + f"    {i.mnemonic:<8} {op_str:<70} @ 0x{i.address:08X} - {bytes_hex}\n")

    if has_instr == False:
        error_func (f, instrs, f"No instructions!")

    return lines

def disassemble_symbol(f):
    if f[0] in addr_done:
        return []  # already written

    if not f[3].startswith("f"):
        lines = dump_data(f)
        return lines

    lines = disassemble_func(f)
    if not lines: # not a valid function after all
        lines = dump_data(f)
    else: # valid function
        blob = sorted(datablob_refs)
        for idx, d in enumerate(blob):
            if d in addr_done:
                continue  # already written
            if d >= f[4] or d < f[0]:
                echo (f"Warn: Attempted to add data addr 0x{d:08X} to {f[2]} (0x{f[0]:08X}), which is out of its bounds.")
                continue
            if idx == len(blob) - 1:
                size = f[4] - d
            else:
                size = blob[idx+1] - d
            for line in dump_data_single(d, size, f, None):
                lines.append(line)
        datablob_refs.clear()
        datablob_ext.clear()
        switchcases.clear()
        switchtable.clear()
    return lines

def assemble_data(addr):

    lines = []
    size = 4
    do_refs = True
    sect = None

    if addr in addr_done:
        return []

    # get size
    if addr in sym_map:
        size = 0
        for sym in ranges_data:
            if addr == sym[0]:
                if sym[3] == "db": # skip bss
                    return []
                sect = sym[3]
                if sym[1] and sym[1] > addr:
                    size = sym[1] - addr # if end addr, get correct size
                break

        if size == 0:
            nextadr = min((a for a in sym_map if a > addr), default=data_end)
            size = nextadr - addr # get next start address in map

    if not sect:
        up = None
        down = None

        for sym in ranges_data:
            if not sym[3].startswith("d"):
                continue

            if sym[0] < addr: # find 
                if (not up) or (sym[0] > up[0]):
                    up = sym
            elif sym[0] > addr:
                if (not down) or (sym[0] < down[0]):
                    down = sym

        if (not (up or down)) or (not (up[3] or down[3])):
            sect = "d"
        elif not (up or up[3]):
            sect = down[3]
        elif not down or down[3]:
            sect = up[3]
        else:
            ddown = addr - down[0] # start of higher addr 
            dup = up[1] - addr     # end of lower addr

            # get nearest addr
            if dup == ddown:  # equals, default down
                sect = down[3]
            elif ddown > dup: # up is near
                sect = up[3]
            else:             # down is near
                sect = down[3]

        sect = sect.replace("r", "").replace("g", "")

    for line in dump_data_single(addr, size, None, sect):
        lines.append(line)

    return lines

def run():
    global data_view, data_start, data_end, sym_map, ranges, noref_list
    sym_map, ranges = load_map()

    count = 0

    upd_status("Reading binary")
    with open(getExeFile(), 'rb') as f:
        data = f.read()
    data_view = memoryview(data)

    md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
    md.detail = True

    clean_dir(getSplitAsmPath())

    upd_status("Preprocessing")
    for f in ranges: # find all data symbols
        if "r" in f[3]: # noref specified
            for a in range(f[0], f[1], 1):
                noref_list.add(a)
        if f[3].startswith("d"):
            size = f[1] - f[0]
            data_addrs.add(f[0])
        else:
            data_start = f[1]

    endaddr = BASE_ADDR + len(data_view) # try find references
    for off in range(0, len(data_view), 4):
        if (off + BASE_ADDR) in noref_list:
            continue
        val = struct.unpack_from("<I", data_view, off)[0]
        if (BASE_ADDR < val < endaddr) and (val not in sym_map):
            if val > data_start:
                dataname = f"dat_{val:08X}"
                sym_map[val] = dataname

    if len(sys.argv) > 1:
        skipToAddr = int(sys.argv[1], 0)
    else:
        skipToAddr = 0

    upd_status("Splecting and writing assembly")

    # Start writing data
    ranges.sort(key=lambda x: x[0]) # sort it once more
    with open(getSplitAsmPath(), 'w') as out:
        out.write(".section .text\n")
        out.write(".syntax unified\n")

        set_status ("Splecting map ")

        # Write out functions
        for f in ranges:
            if f[0] >= data_start:
                continue
            if f[0] < skipToAddr:
                set_progress (f"FF 0x{f[0]:08X}")
                continue
            set_progress (f"0x{f[0]:08X}")
            print_progress()

            lines = disassemble_symbol(f)

            if len(lines) <= 0:
                continue

            count += len(lines)

            out.writelines(lines)

            error_exec()

        set_status ("Splecting data ")

        # Rewrite ranges
        for sym in ranges:
            if sym[3].startswith("d"):
                ranges_data.append(sym)

        # Write out data
        data_end = len(data_view) + BASE_ADDR
        for addr in range(data_start, data_end, 1):
            if addr < skipToAddr:
                set_progress (f"FF 0x{addr:08X}")
                continue
            set_progress (f"0x{addr:08X}")
            print_progress()

            lines = assemble_data(addr)

            if len(lines) <= 0:
                continue

            count += len(lines)

            out.writelines(lines)

    if skipToAddr != 0:
        echo (f"SPLIT INCOMPLETE, STARTED FROM {skipToAddr}")
    echo (f"Wrote {count} lines to {getSplitAsmPath()}")

    # Create dict temp
    data_map_dict = {sym[0]: list(sym) for sym in ranges}

    # start, end, name, typ, next, is_gen, rank
    # go through every known data
    for addr, data in data_symbols_map.items():
        data_start = addr
        data_end = addr + data[0]
        if addr in data_map_dict:  # symbol exists, but update
            sym = data_map_dict[addr]
            sym[1] = data_end
            sym[4] = data_end
            sym[3] = data[1]
            data_map_dict[addr] = sym
        else:  # new, add
            data_map_dict[data_start] = [data_start, data_end, "", data[1], data_end, True, "U"]

    # update all symbols
    for sym in data_map_dict.values():
        if (sym[5]):  # is autogenerated
            sym[2] = ""
        if (addr < data_start) and (not "dl" in sym[3]) and ("d" in f[3]):
            sym[3] = sym[3].replace("d", "dl")  # be sure to mark literal pools
        elif (addr >= data_start) and ("dl" in sym[3]):
            sym[3] = sym[3].replace("dl", "d") # be sure no literal pools are in real data

    # Convert to map syms
    sym_list = [sym_conv(sym) for sym in data_map_dict.values()]

    # Sort
    sym_list.sort(key=lambda x: x[MapFmt.Start])  # sort it

    set_status("Updating map")
    set_progress("")

    updateFull(sym_list)

if __name__ == "__main__":
    run()

