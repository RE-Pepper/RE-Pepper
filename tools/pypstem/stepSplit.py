#!/usr/bin/env python3
import os
from tools.low.glob import *
from tools.splector import split # split asm
from tools.splector import genlist # list splits

def exec_split(clear=False):
    split_list = str(getSplitPath() / "list.cmake")
    miss_path = not getSplitPath().exists()
    miss_list = not os.path.exists(split_list)

    # run
    if clear or (not miss_path and miss_list):
        splector.split.run()
        splector.genlist.run()

    if miss_path:
        fail ("Splits are missing.")
    elif miss_list:
        fail ("Split list missing.")
