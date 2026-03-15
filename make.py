#!/usr/bin/env python3
import sys
import argparse
from tools.pypstem import main as pypstem # build system
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
    parser.add_argument('-d', action='store_true', help="Build with debug info")
    parser.add_argument('-do', action='store_true', help="Build with debug info (objects only)")
    parser.add_argument('-dl', action='store_true', help="Build with debug info (linker only)")
    parser.add_argument('-m', action='store_true', help="Compile only matching code")
    parser.add_argument('-ms', action='store_true', help="Disable shifting during linking")
    parser.add_argument('-w', action='store_true', help="Omit many warnings (nintendo standard)")
    parser.add_argument('-fv', action='store_true', help="Flag: Enable VFE")
    args = parser.parse_args()
    sys.argv = [sys.argv[0]] # clear args
    
    if args.ca:
        args.cr = True
        args.cs = True

    # TODO: remove this hack, upstrem should only contain matches.
    cfg.macros["NON_MATCHING"] = 1
    if args.w:
        # a lot of spammy warnings
        cfg.flags_compile.append("--remarks")
        # default diags found in dwarf info
        cfg.flags_compile.append("--diag_suppress=186,340,401,1256,1297,1568,1764,1786,1788,2523,2819,96,1794,1801,2442,3017,optimizations")
        cfg.flags_compile.append("--diag_error=68,88,174,188,223")
        cfg.flags_compile.append("--diag_warning=177,193,228,550,826,1301")
    if args.m:
        cfg.only_matching = True
    if args.ms:
        cfg.allow_shifting = False
    #if args.k:
    cfg.keep_objects = True
    if args.d or args.do:
        cfg.flags_comppile_cxx.append("--debug")
    if args.d or args.dl:
        cfg.flags_link.append("--debug")

    if args.fv:
        cfg.flags_link.append("--vfemode=force")

    version = pypstem.exec_check(args.version, args.c or args.cr, args.c and not args.cr)

    pypstem.exec_split(args.cs)

    pypstem.exec_build()

    pypstem.exec_export_json()

    pypstem.exec_link()

    pypstem.exec_export_bin()

if __name__ == "__main__":
    main()
