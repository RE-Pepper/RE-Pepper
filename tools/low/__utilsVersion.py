#!/usr/bin/env python3
import os
import sys
import hashlib
from pathlib import Path
from tools.low import cfg

# from _settings
def getProjDir(): # Resolve project path
    return Path(os.path.realpath(__file__).split("tools")[0].rstrip(os.sep))
def getExeFile(): # Path of original code binary
    return str(getVerDir() / "code.bin")
def getHeadFile(): # Path of original code binary
    return str(getVerDir() / "exh.bin")
    
def getVerFile():
    return str(Path(getProjDir()) / "data" / ".version")

def set_ver(version):
    with open(getVerFile(), 'w') as f:
        f.write(version)

def get_ver(version=None):
    if not os.path.exists(getVerFile()):
        set_ver(version or cfg.default_version)
        if not version: print (f"Note: Using default version \'{cfg.default_version}\'")

    with open(getVerFile(), 'r') as f:
        ver = f.read()

    if len(ver) < 2:
        print ("Error: invalid version file")

    return ver

def get_ver_path(version, file):
    return Path(getProjDir()) / "data" / "ver" / version / file

def get_versions():
    return list(cfg.versions.keys())

def is_ver_name(name):
    return name in cfg.versions.keys()

def is_ver_exist(version):
    return os.path.exists(getExeFile(version))

def is_ver_valid(version):
    if not is_ver_name(version):
        return False

    return hashlib.sha256(Path(getExeFile(version)).read_bytes()).hexdigest() == versions[version]
def is_ver_configured(version):
    return os.path.exists(get_ver_path(version, "config.txt")) and os.path.exists(get_ver_path(version, "map.csv"))

def get_file_ver(path):
    target_hash = hashlib.sha256(Path(path).read_bytes()).hexdigest()

    for key, value in cfg.versions.items():
        if value == target_hash:
            return key

    return None

def sort_bin_if_exist():
    try_bin_path = str(Path(getProjDir()) / "data" / "code.bin")
    try_exh_path = str(Path(getProjDir()) / "data" / "exh.bin")

    if not os.path.exists(try_bin_path):
        return None
    if not os.path.exists(try_exh_path):
        fail ("Found unsorted code.bin, but missing exh.bin. Please add exh.bin to data/ (exheader).")

    # Check version
    ver = get_file_ver(try_bin_path)
    if not ver:
        echo ("Found loose data/code.bin, but does not correspond to any known version.")
        echo ("List of versions with SHA256:")
        for k, v in cfg.versions.items():
            print(k + ": " + v)

        fail ("Please verify your binaries, and try again.")

    # Move file
    os.rename(try_bin_path, getExeFile(ver))
    os.rename(try_exh_path, getHeadFile(ver))

    echo (f"found loose binaries in data/, identified as v{ver.upper()} and moved to data/ver/{ver}/.")

    return ver
