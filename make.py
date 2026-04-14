#!/usr/bin/env python3
import sys
import argparse
from tools.pypstem import main as pypstem # build system
from tools.low.glob import * # globals

# TODO: Game is commented out because its a big fuckery when compiling without Stubs, inlines, sym map...
# I guess we have to start again :D (dont want to work with duct tape)

def main():
    parser = argparse.ArgumentParser(description="Build RE:Pepper")
    parser.add_argument("version", nargs="?", default=None, help="Version to use")
    parser.add_argument("--warn", '-w', action='store_true', help="Omit many warnings (nintendo standard)")
    parser.add_argument("--only_matching", '-mo', action='store_true', help="Compile only matching code")
    parser.add_argument("--stop_shifting", '-sh', action='store_true', help="Allow shifts during linking")
    parser.add_argument("--do_split", '-sp', action='store_true', help="Enable splitting process (slow)")
    parser.add_argument("--vfe", '-vf', action='store_true', help="Enable VFE for building")
    parser.add_argument("--debug", '-d', action='store_true', help="Build with debug info")
    parser.add_argument("--delete", '-k', action='store_true', help="Delete temporary built files")
    parser.add_argument("--clean", '-c', action='store_true', help="Clean before building (and stop)")
    parser.add_argument("--clear_all", '-ca', action='store_true', help="Clean split and build (and continue)")
    parser.add_argument("--clear_build", '-cr', action='store_true', help="Clean build (and continue)")
    parser.add_argument("--clear_split", '-cs', action='store_true', help="Clean split (and continue)")
    parser.add_argument("--silent", '-q', action='store_true', help="Silent mode (not added yet)")
    parser.add_argument("--objdiff_donotuse", action='store_true', help="Ignore version parameter (for objdiff)")
    parser.add_argument("--objdiff_full", action='store_true', help="Make objdiff include ALL symbols, even unnamed ones (named)")
    args = parser.parse_args()
    sys.argv = [sys.argv[0]] # clear args

    # first check if objdiff mode is used
    if args.objdiff_donotuse:
        pypstem.exec_objdiff(args.version)
        args.version = None

    # TODO: remove this hack, upstrem should contain matches.
    cfg.macros["NON_MATCHING"] = 1

    # parse arguments
    if args.clear_all:
        args.clear_build = True
        args.clear_split = True

    if args.only_matching:
        cfg.only_matching = True
    if not args.stop_shifting:
        cfg.allow_shifting = True
    if args.do_split:
        cfg.do_split = True
    if args.delete:
        cfg.keep_objects = True
    if args.debug:
        cfg.flags_compile_cxx.append("--debug")
    else:
        cfg.flags_compile_cxx.append("--no_debug")
        cfg.macros["NN_SWITCH_DISABLE_ASSERT_WARNING_FOR_SDK"]=0
        cfg.macros["NN_SWITCH_DISABLE_DEBUG_PRINT_FOR_SDK"]=0
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

    # convert bin to elf
    pypstem.exec_export_elf()

    # split assembly
    pypstem.exec_split(args.clear_split)

    # gen comcom json
    pypstem.exec_export_comcom()

    # build binaries
    is_new = pypstem.exec_build()

    # export objdiff json
    pypstem.exec_export_objdiff(args.objdiff_full)

    if not is_new:
        return

    # link binary
    pypstem.exec_link()

    # export code.bin
    pypstem.exec_export_bin()

if __name__ == "__main__":
    main()
