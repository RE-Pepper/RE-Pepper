#!/usr/bin/env python3
import os
import subprocess
import multiprocessing
import sys
import shutil
import hashlib
import argparse
import splector.split
import splector.genlist

tools.low.__genObjdiffFile import genObjdiff
tools.low.glob import *

def main():
    
    # Clean on command or ver change


    # Split code
    split_list = str(getSplitPath() / "list.cmake")
    if args.cs or not (os.path.exists(getSplitPath()) and os.path.exists(split_list)):
        splector.split.run()
        splector.genlist.run()
    if not os.path.exists(getSplitPath()):
        fail ("Splits are missing.")
    elif not os.path.exists(split_list):
        fail ("Split list missing.")

    # Gen build dir
    if not os.path.isdir(Path(getBuildPath()) / "Makefile"):
        cmake_args = ['cmake', "-B", getBuildPath(), '-G', 'Ninja',
            f"-DRP_VERSION={version.upper()}",
            f"-DRP_SPLIT_LIST={split_list}"
        ]
        if args.m == True:
            cmake_args.append("-DONLY_MATCHING=1")
        if args.w == True:
            cmake_args.append("-DWARNS=1")

        try:
            subprocess.run(cmake_args, check=True)
        except subprocess.CalledProcessError:
            exit(1)
    if not os.path.isdir(getBuildPath()):
        fail ("No cmake generated.")

    # Gen linker
    echo ("Generating linker.ld ...")
    genLDScript()
    if not os.path.exists(Path(getBuildPath()) / "linker.ld"):
        fail ("No linker file generated.")

    # Build
    cmake_args = ['cmake', '--build', getBuildPath(), '--', '-j', str(multiprocessing.cpu_count())]
    if args.v:
        cmake_args.append('VERBOSE=1')
    result = subprocess.run(cmake_args)
    if result.returncode != 0:
        exit(result)

    # Conv .axf to code.bin
    def fromelf():
        echo ("Generating code.bin ...")
        subprocess.run([
            str(Path(os.environ['ARMCC_PATH'], 'bin', 'fromelf').with_suffix('.exe' if sys.platform == 'win32' else '')),
            '--bincombined', str(Path(getBuildPath()) / getElfName()),
            '--output', str(Path(getBuildPath()) / 'code.bin')
        ], check=True)
    fromelf()

    # Copy compile commands for editor
    if os.path.exists(f"{getBuildPath()}/compile_commands.json"):
        shutil.copyfile(f"{getBuildPath()}/compile_commands.json", "compile_commands.json")

    # Gen Objdiff (wip)
    #status("Generating objdiff.json ...")
    #genObjdiff()
