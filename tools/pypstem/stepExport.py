#!/usr/bin/env python3
from tools.pypstem.callProcess import do_export
from tools.pypstem._utils import *
from tools.low.glob import *
from tools.low.genComcom import *
from tools.low.genObjdiff import *

# TODO: objdiff.json

def exec_export_bin():
    if not getElfFile().exists():
        exit(0)

    echo ("Exporting code.bin")
    flags = ["--bincombined", getElfFile(), "--output", getExportFile()]
    do_export(flags)

def exec_export_comcom():
    echo ("Generating json")
    gen_comcom()

def exec_export_objdiff():
    if not getBuildPath().is_dir():
        exit(0)

   # echo ("Generating objdiff")
   # gen_objdiff()
