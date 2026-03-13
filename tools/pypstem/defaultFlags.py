#!/usr/bin/env python3

default_flags_comp = [
    "--cpu=MPCore",
    "--fpmode=fast",
    "--apcs=/interwork",
]  # --info=totals

default_flags_comp_asm = [
    "--diag_suppress=1608",
]

default_flags_comp_cxx = [
    "--signed_chars",
    "--dollar",
    "--force_new_nothrow",
    "--no_rtti",
    "--no_debug",
    "--no_debug_macros",
]

default_flags_link = [
    "--verbose", "--xref",
    "--cpu=MPCore",
    "--fpu=VFPv2",
    "--startup=__ctr_start",
    "--entry=__ctr_start",
    "--keep=nnMain",
    "--datacompressor=off",
    "--mangled",
    "--symbols",
    "--map",
    "--muldefweak",
    "--no_debug",
    "--diag_suppress=6642,6439,6314",
]

