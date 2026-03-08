#!/usr/bin/env python3
from tools.pypstem.callProcess import do_export
from tools.pypstem._utils import *
from tools.low.glob import *
from tools.low.__genComcom import *
from tools.low.__genObjdiff import *

# TODO: objdiff.json

def exec_export_bin():
    if not getElfFile().exists():
        exit(0)

    echo ("Exporting code.bin")
    do_export(f"--bincombined {getElfFile()} --output {getExportFile()}")

def exec_export_json():
    if not getBuildPath().is_dir():
        exit(0)

    echo ("Generating compiler_commands.json")
    gen_comcom()

   # echo ("Generating objdiff.json")
   # gen_objdiff()
