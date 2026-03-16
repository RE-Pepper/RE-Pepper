#!/usr/bin/env python3
import os
import sys
import hashlib
from pathlib import Path
from tools.low import cfg

# from _settings
def getVerDir(version):
    return Path(getProjDir()) / "data" / "ver" / version
def getProjDir(): # Resolve project path
    return Path(os.path.realpath(__file__).split("tools")[0].rstrip(os.sep))
def getBinFile(version): # Path of original code binary
    return getVerDir(version) / "code.bin"
def getHeadFile(version): # Path of original code binary
    return getVerDir(version) / "exh.bin"
def echo(str, end="\n"):
    print (f"\033[38;5;221m{str}\033[0m\033[K", end=end)
def fail(err):
    print (f"\033[38;5;196mError: {err}\033[0m\033[K")
    exit(1)
    
def getVerFile():
    return str(Path(getProjDir()) / "data" / ".version")

def write_ver(version):
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
    return getVerDir(version) / file

def get_versions():
    return list(cfg.versions)

def is_ver_name(name):
    return name in cfg.versions

def is_ver_exist(version):
    return getBinFile(version).exists()

def is_ver_valid(version):
    if not is_ver_name(version):
        return False

    return hashlib.sha256(getBinFile(version).read_bytes()).hexdigest() == cfg.versions[version]
def is_ver_configured(version):
    return getVerDir(version).exists() and get_ver_path(version, "map.csv").exists()

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
    os.rename(try_bin_path, getBinFile(ver))
    os.rename(try_exh_path, getHeadFile(ver))

    echo (f"Found loose binaries in data/, identified as v{ver.upper()} and moved to data/ver/{ver}/.")

    return ver
