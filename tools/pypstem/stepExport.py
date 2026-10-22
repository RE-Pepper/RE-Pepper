#!/usr/bin/env python3
from tools.pypstem.callProcess import do_export
from tools.pypstem._utils import *
from tools.low.glob import *
from tools.low.genComcom import *
from tools.low.genObjdiff import *

def exec_export_bin():
    if not getElfFile().exists():
        exit(0)

    echo ("Exporting code.bin")
    flags = ["--bincombined", getElfFile(), "--output", getExportFile()]
    do_export(flags)

    if cfg.matching:
        # fromelf stops at the last loadable byte, the original carries
        # the makerom RW page padding. pad back to the original length,
        # cut anything beyond (bss pins/spill, the check tool reports it)
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
                echo (f"Trimmed {build_len - orig_len} bytes beyond the original image (bss pins/spill, see tools/diff.py)")

            # the original's RW page padding is zero, but the spill's
            # sections land in the same page. zero the range after the
            # RW section so the exported page matches the original.
            from tools.low.readHeader import read_header, HeadType, HeadVal
            hdr = read_header()
            rw_hi_off = hdr[HeadType.Rw][HeadVal.End] - hdr[HeadType.Text][HeadVal.Start]
            if 0 < rw_hi_off < orig_len:
                with open(getExportFile(), "r+b") as f:
                    f.seek(rw_hi_off)
                    f.write(b"\x00" * (orig_len - rw_hi_off))
                echo (f"Zeroed RW page padding 0x{rw_hi_off:X}..0x{orig_len:X}")

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
