#!/usr/bin/env python3
import sys
import argparse
from tools import pypstem # build system
from tools.low.glob import * # globals

# todo: only matching mode
def main():
    parser = argparse.ArgumentParser('make.py', description="Build the Super Mario 3D Land decompilation project")
    parser.add_argument("version", nargs="?", default=None, help="Version to use")
    parser.add_argument('-c', action='store_true', help="Clean before building")
    parser.add_argument('-cs', action='store_true', help="Clean split before building")
    parser.add_argument('-v', action='store_true', help="Give verbose output")
    parser.add_argument('-m', action='store_true', help="Compile only matching code")
    parser.add_argument('-w', action='store_true', help="Omit many warnings (nintendo standard)")
    args = parser.parse_args()
    sys.argv = [sys.argv[0]] # clear args

    version = pypstem.exec_check(args.version, args.c)

    pypstem.exec_split(args.cs)

    pypstem.exec_build()

    pypstem.exec_link()

    pypstem.exec_export()

if __name__ == "__main__":
    main()
