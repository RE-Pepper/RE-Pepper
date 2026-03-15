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
        fail_ex (f"Compiler version invalid: {ver}", f"Example format: \"4.1/844\"")

    return ver.split("/")

def getCompilerPath(rev, build):
    return getCompilersDir() / rev / build

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
    out = getCompilersDir() / "wibo"
    if out.exists():
        return

    download("wibo", out, "wibo", False)
    link = "https://github.com/RedPepperDec/data/releases/download/dasdasdsa/wibo"
    os.chmod(out, 0o755)

def setup_compiler(ver=getCompilerVer()):
    if not ver:
        ver = getCompilerVer()
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

    os.environ[get_compiler_env_inc(rev)] = dir_inc
    os.environ[get_compiler_env_lib(rev)] = dir_lib

    setCompilerPath(dir)
    setCompilerVer(ver)

def get_compiler_env_inc(rev=getCompilerVer()):
    if rev.startswith("4.0"):
        return "RVCT40INC"
    elif rev.startswith("4.1"):
        return "ARMCC41INC"
    elif rev.startswith("5.04"):
        return "ARMCC5INC"
    else:
        fail(f"Compiler revision not recognized: {rev}")

def get_compiler_env_lib(rev=getCompilerVer()):
    if rev.startswith("4.0"):
        return "RVCT40LIB"
    elif rev.startswith("4.1"):
        return "ARMCC41LIB"
    elif rev.startswith("5.04"):
        return "ARMCC5LIB"
    else:
        fail(f"Compiler revision not recognized: {rev}")
