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

    if cfg.matching:
        # The original code.bin carries the page alignment padding of the
        # RW section (all zero, added by makerom). fromelf stops at the
        # last loadable byte, so pad the export back to the original
        # file length. Content beyond the original span (pinned bss
        # sections, spill) is cut from the export, the check tool
        # reports it from the linker map instead.
        orig = getBinCodeFile()
        if orig.exists():
            orig_len = orig.stat().st_size
            build_len = getExportFile().stat().st_size
            if build_len < orig_len:
                with open(getExportFile(), "ab") as f:
                    f.write(b"\x00" * (orig_len - build_len))
                echo (f"Padded {orig_len - build_len} bytes of RW page alignment")
            elif build_len > orig_len:
                with open(getExportFile(), "r+b") as f:
                    f.truncate(orig_len)
                echo (f"Trimmed {build_len - orig_len} bytes beyond the original image (bss pins/spill, see checkMatch)")

def exec_export_elf():
    if not getBinCodeFile().exists():
        return
    if not isSymMapDiff() and getBinCodeFile().with_suffix(".elf").exists():
        return

    echo ("Converting bin to elf")

    from tools.low.convBinToElf import conv_bin_to_elf
    conv_bin_to_elf()

def exec_export_comcom():
    gen_comcom()

def exec_export_objdiff():
    if not getBuildPath().is_dir():
        exit(0)

    echo ("Generating objdiff")
    gen_objdiff()
