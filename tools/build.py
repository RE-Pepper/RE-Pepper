#!/usr/bin/env python3
import os
import subprocess
import multiprocessing
from colorama import Fore, Style
import sys
import shutil
import hashlib
import argparse
import splector.split
import splector.genlist

from low.__genLinkerScript import genLDScript
from low.__genObjdiffFile import genObjdiff
from low.__utilsVer import *
from _settings import *

def main() -> None:
    def status(msg: str):
        print(Fore.CYAN + msg + Fore.RESET + Style.RESET_ALL)

    parser = argparse.ArgumentParser('build.py', description="Build the Super Mario 3D Land decompilation project")
    parser.add_argument("version", nargs="?", default=None, help="Version to use")
    parser.add_argument('-c', action='store_true', help="Clean before building")
    parser.add_argument('-cs', action='store_true', help="Clean split before building")
    parser.add_argument('-v', action='store_true', help="Give verbose output")
    parser.add_argument('-m', action='store_true', help="Compile only matching code (BROKEN)")
    parser.add_argument('-w', action='store_true', help="Omit many warnings (nintendo format)")
    args = parser.parse_args()
    sys.argv = [sys.argv[0]] # clear args
    
    # Preparations and check version
    version = args.version
    found_version = sort_bin_if_exist()
    old_version = get_ver(version)

    if not version or found_version or ("code.bin" in version):
        version = found_version or old_version
    else:
        if version == "us":
            version = "us_1"
        if not is_ver_name(version):
            print (f"Passed argument \'{version}\' is not a valid version!")
            print (f"Available versions: {get_versions()}")
            sys.exit(1)

        if found_version and (found_version is not version):
            print ("found unsorted code.bin in data/, but parameter version differs.")
            print ("data/code.bin: " + found_version + ", specified: " + version)
            sys.exit(1)

        set_ver(version)

    if not is_ver_exist(version):
        print(f"data/ver/{version}/code.bin missing. Please provide the code.bin from the {version} version.")
        set_ver(old_version)
        return
    if not is_ver_valid(version):
        print(f"code.bin for {version} is invalid. Did you dump the right version, correctly?")
        set_ver(old_version)
        return
    if not is_ver_configured(version):
        print(f"Current version {version} is not configured. Try again later, por favor.")
        set_ver(old_version)
        return

    # Clean on command or ver change
    if args.c or (version != old_version):
        subprocess.run(["cmake", "--build", getBuildPath(), "--target", "clean"])
        if args.c:
            exit(0)
        else:
            print(f"Version changed, rebuilding. ({old_version.upper()} -> {version.upper()})")

    status (f"RedPepper v{version.upper()}")

    # Split code
    split_list = str(getSplitPath() / "list.cmake")
    if args.cs or not (os.path.exists(getSplitPath()) and os.path.exists(split_list)):
        splector.split.run()
        splector.genlist.run()
    if not os.path.exists(getSplitPath()):
        status ("Splits are missing.")
        return
    elif not os.path.exists(split_list):
        status ("Split list missing.")
        return

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
        status ("No cmake generated.")

    # Gen linker
    status ("Generating linker.ld ...")
    genLDScript()
    if not os.path.exists(Path(getBuildPath()) / "linker.ld"):
        status ("No linker file generated.")
        return

    # Build
    cmake_args = ['cmake', '--build', getBuildPath(), '--', '-j', str(multiprocessing.cpu_count())]
    if args.v:
        cmake_args.append('VERBOSE=1')
    result = subprocess.run(cmake_args)
    if result.returncode != 0:
        exit(result)

    # Conv .axf to code.bin
    def fromelf():
        status("Generating code.bin ...")
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

if __name__ == "__main__":
    main()
