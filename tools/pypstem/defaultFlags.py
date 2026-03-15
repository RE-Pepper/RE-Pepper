#!/usr/bin/env python3

default_flags_comp = [
    "--cpu=MPCore",
    "--fpmode=fast",
    "--apcs=/interwork",
]

default_flags_comp_asm = [
    "--diag_suppress=1608",
]

default_flags_comp_cxx = [
    "--signed_chars",
    "--dollar",
    "--force_new_nothrow",
    "--no_rtti",
    "--debug",
    "--no_debug_macros",
]

default_flags_link = [
    "--verbose",
    "--debug",
    "--cpu=MPCore",
    "--fpu=VFPv2",
    "--startup=__ctr_start",
    "--entry=__ctr_start",
    "--keep=nnMain",
    "--datacompressor=off",
    "--mangled",
    "--symbols",
    "--map",
    "--diag_suppress=6642,6439,6329,6314",
]

