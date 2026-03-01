#!/usr/bin/env python3
import os
import sys
import struct
from _settings import *
from enum import IntEnum

def fail(msg: str):
    print(msg)
    sys.exit(1)

class HeadType(IntEnum):
    Text = 0
    Ro = 1
    Rw = 2
    Bss = 3
class HeadVal(IntEnum):
    Start = 0
    End = 1

def readHeader():
    if not os.path.isfile(getHeadFile()):
        fail (f"Missing exh.bin for v{get_ver().upper()}")
    
    with open(getHeadFile(), 'rb') as f:
        data = f.read(0x40)

    if data[:6] != getAppName():
        fail (f"Invalid exh.bin for v{get_ver().upper()}: Expected {getAppName}, got {data[:6]}")

    text_addr, _, text_size = struct.unpack('<III', data[0x10:0x1C])
    ro_addr, _, ro_size = struct.unpack('<III', data[0x20:0x2C])
    rw_addr, _, rw_size = struct.unpack('<III', data[0x30:0x3C])
    bss_size = struct.unpack('<I', data[0x3C:0x40])[0]
    bss_addr = rw_addr + rw_size

    return [
        [text_addr, text_addr + text_size],
        [ro_addr, ro_addr + ro_size],
        [rw_addr, rw_addr + rw_size],
        [bss_addr, bss_addr + bss_size]
    ]
