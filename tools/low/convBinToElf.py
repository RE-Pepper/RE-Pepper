#!/usr/bin/env python3
from struct import pack, unpack
from sys import path

from tools.low.glob import *
from tools.low.readHeader import *
from tools.low.readSymMap import *
from tools.low.getSection import typeToSection

def conv_bin_to_elf():
    if not getBinCodeFile():
        echo ("conv_bin_to_elf called, but no code.bin exists. Ignoring.")
        return

    header = read_header()

    for htype in HeadType:
        start = header[htype][HeadVal.Start]
        end = header[htype][HeadVal.End]
        size = end - start
        echo(f"{htype.name:.<10} 0x{start:08X} - 0x{end:08X} | 0x{size:08X}")

    with open(getBinCodeFile(), "rb") as f:
        full_bin_data = f.read()

    shstrtab = b"\x00"
    strtab = b"\x00"
    
    mapping_list = [b"\x00" * 0x10]
    locals_list = []
    globals_list = []
    
    func_sections_headers = []
    base_off = 0x10000
    
    # Section 0 is NULL. Symbols start assigning from Index 1.
    sect_idx = 1
    raw_syms = read_sym_file()

    for sym in raw_syms:
        if not sym[MapFmt.Symbol]:
            continue
        if "d" in sym[MapFmt.Type]:
            continue

        addr = sym[MapFmt.Start]
        name = sym[MapFmt.Symbol]
        typ = sym[MapFmt.Type]
        end = sym[MapFmt.End]

        if addr >= header[HeadType.Bss][HeadVal.End]:
            fail (f"Symbol addr 0x{addr:08X} is too big!")
        elif addr < header[HeadType.Text][HeadVal.Start]:
            fail (f"Symbol addr 0x{addr:08X} is too small!")

        sym_size = end - addr if end else 0
        
        # Logic for section name, type, and flags
        s_name = name
        s_type = 1 # PROGBITS
        s_flags = 0
        
        if "f" in typ:
            if not name: name = f"fn_{addr:08X}"
            info = 2
            map_sym = b"$t\x00" if addr % 2 != 0 else b"$a\x00"
            s_flags = 6 # AX
        else:
            if not name: name = f"dat_{addr:08X}"
            info = 1
            map_sym = b"$d\x00"
            if addr >= header[HeadType.Bss][HeadVal.Start]:
                s_type = 8 # NOBITS
                s_flags = 3 # WA
            elif addr >= header[HeadType.Rw][HeadVal.Start]:
                s_flags = 3 # WA
            else:
                s_flags = 2 # A

        sh_name_ptr = len(shstrtab)
        name_bytes = name.encode() + b"\x00"
        shstrtab += name_bytes
        
        s_off = 0
        if s_type != 8:
            s_off = base_off + (addr - header[HeadType.Text][HeadVal.Start])
        
        func_sections_headers.append(pack("<10I", 
            sh_name_ptr, s_type, s_flags, addr, s_off, sym_size, 0, 0, 4, 0
        ))

        # Mapping symbols
        m_off = len(strtab); strtab += map_sym
        mapping_list.append(pack("<IIIBBH", m_off, addr & ~1, 0, 0, 0, sect_idx))

        # Main symbols
        name_sym = len(strtab); strtab += name_bytes
        if "g" in typ:
            globals_list.append(pack("<IIIBBH", name_sym, addr, sym_size, (1 << 4) | info, 0, sect_idx))
        else:
            locals_list.append(pack("<IIIBBH", name_sym, addr, sym_size, (0 << 4) | info, 0, sect_idx))
            
        sect_idx += 1

    # Table indices
    shstr_name_off = len(shstrtab); shstrtab += b".shstrtab\x00"
    strtab_name_off = len(shstrtab); shstrtab += b".strtab\x00"
    symtab_name_off = len(shstrtab); shstrtab += b".symtab\x00"

    shstr_idx = sect_idx; sect_idx += 1
    str_idx = sect_idx; sect_idx += 1
    sym_idx = sect_idx; sect_idx += 1

    num_locals = len(mapping_list) + len(locals_list)
    symtab = b"".join(mapping_list) + b"".join(locals_list) + b"".join(globals_list)
    strtab += b"\x00" * ((4 - (len(strtab) % 4)) % 4)
    
    data_size = len(full_bin_data)
    tables_off = (base_off + data_size + 0xFF) & ~0xFF

    def align(x, a):
        return (x + (a - 1)) & ~(a - 1)
    shstrtab_off = tables_off
    strtab_off   = align(shstrtab_off + len(shstrtab), 4)
    symtab_off   = align(strtab_off   + len(strtab), 4)
    sht_off      = align(symtab_off   + len(symtab), 4)

    with open(getBinCodeFile().with_suffix(".elf"), "wb") as f:
        f.write(b"\x7FELF\x01\x01\x01\x00" + b"\x00" * 8)
        f.write(pack("<HHI", 2, 0x28, 1))
        f.write(pack("<III", header[HeadType.Text][HeadVal.Start], 0x34, sht_off))
        f.write(pack("<I6H", 0x5000002, 0x34, 0x20, 1, 0x28, sect_idx, shstr_idx))
        
        f.write(pack("<8I", 1, base_off, header[HeadType.Text][HeadVal.Start], header[HeadType.Text][HeadVal.Start], data_size, data_size, 7, 0x1000))

        # write the data
        f.write(b"\x00" * (base_off - f.tell()))
        f.write(full_bin_data)

        # Write the debug info
        f.write(b"\x00" * (shstrtab_off - f.tell()))
        f.write(shstrtab)
        f.write(b"\x00" * (strtab_off - (shstrtab_off + len(shstrtab))))
        f.write(strtab)
        f.write(b"\x00" * (symtab_off - (strtab_off + len(strtab))))
        f.write(symtab)
        f.write(b"\x00" * (sht_off - (symtab_off + len(symtab))))

        f.write(b"\x00" * 0x28) # Section 0
        for h in func_sections_headers:
            f.write(h)
        
        f.write(pack("<10I", shstr_name_off, 3, 0, 0, shstrtab_off, len(shstrtab), 0, 0, 1, 0))
        f.write(pack("<10I", strtab_name_off, 3, 0, 0, strtab_off, len(strtab), 0, 0, 1, 0))
        f.write(pack("<10I", symtab_name_off, 2, 0, 0, symtab_off, len(symtab), str_idx, num_locals, 4, 16))
