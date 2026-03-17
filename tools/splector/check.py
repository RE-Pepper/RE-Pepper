#!/usr/bin/env python3
import os
import sys
from _utils import *

md = None

def main():
    sym_map, ranges = load_map()

    for i, f in enumerate(ranges):
        if i == len(ranges)-1:
            continue

        next = ranges[i+1]
        if f[1] != next[0]:
            print (f"Addr Hole from 0x{f[1]:08X} to 0x{next[0]:08X}")

if __name__ == "__main__":
    main()
