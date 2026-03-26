#!/usr/bin/env python3
import os
import sys
import struct
from enum import IntEnum

from tools.low.glob import *

# Read Ext Header from game (exheader.bin) and get section offsets

class HeadType(IntEnum):
    Text = 0
    Ro = 1
    Rw = 2
    Bss = 3
class HeadVal(IntEnum):
    Start = 0
    End = 1

def read_header():
    text_addr = text_size = 0
    ro_addr = ro_size = 0
    rw_addr = rw_size = 0
    bss_addr = bss_size = 0

    if getBinAxfFile().exists():
        fromelf_flags = [str(getBinFile())]

        from tools.pypstem.callProcess import do_export
        lines = do_export(fromelf_flags, False, True).strip().splitlines()
        for line_i, line in enumerate(lines):
            if not "** Section #" in line:
                continue

            if line_i+3 > len(lines):
                continue
            if not "Address" in lines[line_i+2]:
                continue
            sect_name = line.split()[3].replace("\'", "")
            sect_addr = int(lines[line_i+2].split()[1], 0)
            sect_size = int(lines[line_i+1].split()[2])

            if sect_name == "STUP_ENTRY":
                text_addr = sect_addr
                text_size = sect_size
            elif sect_name == "RO":
                ro_addr = sect_addr
                ro_size = sect_size
            elif sect_name == "RW":
                rw_addr = sect_addr
                rw_size = sect_size
            elif sect_name == "ZI":
                bss_addr = sect_addr
                bss_size = sect_size
    else:
        if not getHeadFile().exists():
            fail (f"Missing exh.bin for v{getVersion().upper()}")
        
        with open(getHeadFile(), 'rb') as f:
            data = f.read(0x40)

        app_name = cfg.app_name.encode()
        if data[:6] != app_name:
            fail (f"Invalid exh.bin for v{getVersion().upper()}: Expected {app_name}, got {data[:6]}")

        text_addr, _, text_size = struct.unpack('<III', data[0x10:0x1C])
        ro_addr, _, ro_size = struct.unpack('<III', data[0x20:0x2C])
        rw_addr, _, rw_size = struct.unpack('<III', data[0x30:0x3C])
        bss_size = struct.unpack('<I', data[0x3C:0x40])[0]
        bss_addr = rw_addr + rw_size

    # return it
    return [
        [text_addr, text_addr + text_size],
        [ro_addr, ro_addr + ro_size],
        [rw_addr, rw_addr + rw_size],
        [bss_addr, bss_addr + bss_size]
    ]
