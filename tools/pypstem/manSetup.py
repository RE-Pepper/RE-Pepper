#!/usr/bin/env python3
import os
import io
import shutil
import zipfile
import requests
import urllib.request
from tools.low.glob import *

# input: "4.1/844"
# output: ["4.1", "844"]
def splitVersion(ver):
    if not ver:
        fail ("Compiler version cannot be found.")
    if not "/" in ver or ver.count("/") != 1:
        fail (f"Compiler version invalid: {ver}", f"Example format: \"4.1/844\"")

    return ver.split("/")

def getCompilerPath(rev, build):
    return getCompilerDir() / rev / build

def download(rev, build):
    dir = getCompilerPath(rev, build)
    if dir.is_dir():
        fail ("Bug: download called, even though version exists.", f"Version: {ver}")

    dir.mkdir(parents=True, exist_ok=True)

    echo (f"Downloading compiler {rev}/{build} ...")

    link = f"https://github.com/RedPepperDec/data/releases/download/dasdasdsa/{build}.zip"
    try:
        with urllib.request.urlopen(link) as response:
            with zipfile.ZipFile(io.BytesIO(response.read())) as z:
                dir.mkdir(parents=True, exist_ok=True)
                z.extractall(dir)

    except Exception as e:
        if dir.exists():
            shutil.rmtree(dir)

        fail (f"Download failed: {e}")

def check_wibo():
    if not isLinux():
        return
    out = getCompilerDir() / "wibo"
    if os.path.exists(out):
        return

    echo ("Downloading wibo ...")

    out.parent.mkdir(parents=True, exist_ok=True)
    link = "https://github.com/decompals/wibo/releases/download/1.1.0/wibo-x86_64"
    out.write_bytes(requests.get(link).content)
    os.chmod(out, 0o755)

def setup_compiler(ver):
    rev, build = splitVersion(ver)

    dir = getCompilerPath(rev, build)

    if not dir.is_dir(): # download when missing
        download(rev, build)

    if not dir.is_dir(): # still missing
        fail (f"Cannot get compiler {ver}: Directory not found.")
    if not Path(dir / "bin" / "armcc.exe").exists():
        fail (f"Cannot get compiler {ver}: Invalid or empty folder.")

    dir_lib = str(dir / "lib")
    dir_inc = str(dir / "include")

    match rev:
        case "4.0":
            # RVCT
            os.environ["RVCT40INC"] = dir_inc
            os.environ["RVCT40LIB"] = dir_lib
        case "4.1":
            # ARMCC 4X
            os.environ["ARMCC4INC"] = dir_inc
            os.environ["ARMCC4LIB"] = dir_lib
        case "5.04":
            # ARMCC 5X
            os.environ["ARMCC5INC"] = dir_inc
            os.environ["ARMCC5LIB"] = dir_lib
        case _:
            fail (f"Compiler revision not recognized: {rev}")

    return dir / "bin"
