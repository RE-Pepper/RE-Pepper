#!/usr/bin/env python3
import sys
import argparse
from tools import pypstem # build system
from tools.low.glob import * # globals

# TODO: Game is commented out because its a big fuckery when compiling without Stubs, inlines, sym map...
# I guess we have to start again :D (dont want to work with duct tape)

def main():
    parser = argparse.ArgumentParser('make.py', description="Build the Super Mario 3D Land decompilation project")
    parser.add_argument("version", nargs="?", default=None, help="Version to use")
    parser.add_argument('-c', action='store_true', help="Clean before building (and stop)")
    parser.add_argument('-cr', action='store_true', help="Clean before building (and continue)")
    parser.add_argument('-cs', action='store_true', help="Clean split and continue")
    parser.add_argument('-ca', action='store_true', help="Clean split and build and continue")
    #parser.add_argument('-k', action='store_true', help="Keep built output (for debugging)")
    parser.add_argument('-m', action='store_true', help="Compile only matching code")
    parser.add_argument('-s', action='store_true', help="Deny shifting during linking")
    parser.add_argument('-w', action='store_true', help="Omit many warnings (nintendo standard)")
    parser.add_argument('-fv', action='store_true', help="Flag: Enable VFE")
    args = parser.parse_args()
    sys.argv = [sys.argv[0]] # clear args
    
    if args.ca:
        args.cr = True
        args.cs = True

    if args.w:
        cfg.flag_diag += "--diag_suppress=186,340,401,1256,1297,1568,1764,1786,1788,2523,2819,96,1794,1801,2442,3017,optimizations --diag_error=68,88,174,188,223 --diag_warning=177,193,228,550,826,1301"
    if args.m:
        cfg.only_matching = False

    # TODO: remove this hack, upstrem should only contain matches.
    cfg.macros["NON_MATCHING"] = 1
    if args.s:
        cfg.allow_shifting = False
    #if args.k:
    cfg.keep_objects = True

    if args.fv:
        cfg.flags_link += "--vfemode=force"

    version = pypstem.exec_check(args.version, args.c or args.cr, args.c and not args.cr)

    pypstem.exec_split(args.cs)

    pypstem.exec_build()

    pypstem.exec_export_json()

    pypstem.exec_link()

    pypstem.exec_export_bin()

if __name__ == "__main__":
    main()
