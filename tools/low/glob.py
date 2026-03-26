#!/usr/bin/env python3
import os

from tools.low.utils import *

# moved everything to low/utils

# enable ansi colors on windows
if os.name == "nt":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
    mode = ctypes.c_uint()
    kernel32.GetConsoleMode(handle, ctypes.byref(mode))
    kernel32.SetConsoleMode(handle, mode.value | 0x0004)

# read config
cfg.read(getVerDir(), getDataDir())
setCompilerVer(cfg.compiler)

