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

    # Build
    cmake_args = ['cmake', '--build', getBuildPath(), '--', '-j', str(multiprocessing.cpu_count())]
    if args.v:
        cmake_args.append('VERBOSE=1')
    result = subprocess.run(cmake_args)
    if result.returncode != 0:
        exit(result)

