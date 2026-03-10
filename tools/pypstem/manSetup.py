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

def download(name_file, path, name_show, is_zip):
    echo (f"Downloading {name_show} ...")

    link = f"https://github.com/RedPepperDec/data/releases/download/dasdasdsa/{name_file}.zip"

    try:
        if is_zip:
            path.mkdir(parents=True, exist_ok=True)
            with urllib.request.urlopen(link) as response:
                with zipfile.ZipFile(io.BytesIO(response.read())) as z:
                    path.mkdir(parents=True, exist_ok=True)
                    z.extractall(path)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(requests.get(link).content)

    except Exception as e:
        if path.exists():
            shutil.rmtree(path)

        fail (f"Download for {name_show} failed: {e}")

def check_wibo():
    if not isLinux():
        return
    out = getCompilerDir() / "wibo"
    if out.exists():
        return

    download("wibo", out, "wibo", False)
    link = "https://github.com/RedPepperDec/data/releases/download/dasdasdsa/wibo"
    os.chmod(out, 0o755)

def setup_compiler(ver):
    rev, build = splitVersion(ver)

    dir = getCompilerPath(rev, build)

    if not dir.is_dir(): # download when missing
        download(build, dir, f"compiler {rev}/{build}", True)

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
