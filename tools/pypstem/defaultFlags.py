#!/usr/bin/env python3

default_flags_comp = [
    "--cpu=MPCore",
    "--fpmode=fast",
    "--apcs=/interwork",
    "--depend_format=unix_quoted",
]

default_flags_comp_asm = [
    "--diag_suppress=1608",
]

default_flags_comp_cxx = [
    "--signed_chars",
    "--dollar",
    "--force_new_nothrow",
    "--no_rtti",
    "--no_debug_macros",
    "--no_depend_system_headers",
]

default_flags_link = [
    "--verbose",
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
    "--muldefglobal",
    "--diag_suppress=6642,6439,6329,6314",
]

