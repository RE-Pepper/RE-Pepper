#!/usr/bin/env python3
import os
from pathlib import Path
from _settings import *
from splector._utils import *

def run():
    echor ("Writing cmake list ...")

    # in path exist?
    if not os.path.exists(getSplitPath()):
        fail (f"{getSplitPath()} not found.")

    # grab asm files
    in_files = getSplitPath().glob("*.s")
    if not in_files:
        fail (f"{getSplitPath()} is empty.")

    with open(getSplitPath() / "list.cmake", 'w') as out:
        out.write("set(SPLIT_LIST")
        for in_file in in_files:
            out.write(f"\n\t")
            out.write(str(in_file))
        out.write("\n)\n")

    echo (f"Wrote cmake list.")

