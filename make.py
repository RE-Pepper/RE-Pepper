#!/usr/bin/env python3
import sys
import argparse
from tools.pypstem import main as pypstem # build system
from tools.low.glob import * # globals

# TODO: Game is commented out because its a big fuckery when compiling without Stubs, inlines, sym map...
# I guess we have to start again :D (dont want to work with duct tape)

def main():
    parser = argparse.ArgumentParser('make.py', description="Build RE:Pepper")
    parser.add_argument("version", nargs="?", default=None, help="Version to use")
    parser.add_argument("--warn", '-w', action='store_true', help="Omit many warnings (nintendo standard)")
    parser.add_argument("--match_only", '-mo', action='store_true', help="Compile only matching code")
    parser.add_argument("--shift", '-sh', action='store_true', help="Allow shifts during linking")
    parser.add_argument("--split", '-sp', action='store_true', help="Enable splitting process (slow)")
    parser.add_argument("--vfe", '-vf', action='store_true', help="Enable VFE for building")
    parser.add_argument("--debug", '-d', action='store_true', help="Build with debug info")
    parser.add_argument("--debug_obj", '-do', action='store_true', help="Build with debug info (objects only)")
    parser.add_argument("--debug_link", '-dl', action='store_true', help="Build with debug info (linker only)")
    parser.add_argument("--delete", '-k', action='store_true', help="Delete temporary built files")
    parser.add_argument("--clean", '-c', action='store_true', help="Clean before building (and stop)")
    parser.add_argument("--clear_all", '-ca', action='store_true', help="Clean split and build (and continue)")
    parser.add_argument("--clear_build", '-cr', action='store_true', help="Clean build (and continue)")
    parser.add_argument("--clear_split", '-cs', action='store_true', help="Clean split (and continue)")
    args = parser.parse_args()
    sys.argv = [sys.argv[0]] # clear args

    # TODO: remove this hack, upstrem should only contain matches.
    cfg.macros["NON_MATCHING"] = 1

    # parse arguments
    if args.clear_all:
        args.clear_build = True
        args.clear_split = True
    if args.debug:
        args.debug_obj = True
        args.debug_link = True

    if args.match_only:
        cfg.only_matching = True
    if args.shift:
        cfg.allow_shifting = True
    if args.split:
        cfg.do_split = True
    if args.delete:
        cfg.keep_objects = True
    if args.debug_obj:
        cfg.flags_comppile_cxx.append("--debug")
    if args.debug_link:
        cfg.flags_link.append("--debug")
    if args.vfe:
        cfg.flags_link.append("--vfemode=force")
    if args.warn:
        # a lot of spammy warnings
        cfg.flags_compile.append("--remarks")
        # default diags found in dwarf info
        cfg.flags_compile.append("--diag_suppress=186,340,401,1256,1297,1568,1764,1786,1788,2523,2819,96,1794,1801,2442,3017,optimizations")
        cfg.flags_compile.append("--diag_error=68,88,174,188,223")
        cfg.flags_compile.append("--diag_warning=177,193,228,550,826,1301")

    # starting

    # version and clear checks
    pypstem.exec_check(args.version, args.clean or args.clear_build, args.clean and not args.clear_build)

    # split assembly
    pypstem.exec_split(args.clear_split)

    # build binaries
    pypstem.exec_build()

    # export json files
    pypstem.exec_export_json()

    # link binary
    pypstem.exec_link()

    # export code.bin
    pypstem.exec_export_bin()

if __name__ == "__main__":
    main()
