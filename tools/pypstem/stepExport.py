#!/usr/bin/env python3
from tools.pypstem.callProcess import do_export
from tools.pypstem._utils import *
from tools.low.glob import *
from tools.low.genComcom import *
from tools.low.getIsMapDiff import *

def exec_export_bin():
    if not getElfFile().exists():
        return

    echo ("Exporting code.bin")
    flags = ["--bincombined", getElfFile(), "--output", getExportFile()]
    do_export(flags)

def exec_export_elf():
    if not getBinCodeFile().exists():
        return
    if not is_sym_map_diff():
        return

    echo ("Converting bin to elf")

    from tools.low.convBinToElf import conv_bin_to_elf
    conv_bin_to_elf()

def exec_export_comcom():
    echo ("Generating json")
    gen_comcom()

def exec_export_objdiff(do_full_file=False):
    if not is_sym_map_diff():
        return
    if not getBuildPath().is_dir():
        fail ("Build path is missing?!")

    from tools.low.genObjdiff import gen_objdiff

    echo ("Generating objdiff")
    gen_objdiff(do_full_file)
