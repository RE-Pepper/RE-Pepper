#!/usr/bin/env python3
import os
import sys
import hashlib
from pathlib import Path

from tools.low import cfg
from tools.low.glob import *

def write_ver(version):
    with open(getCfgVerFile(), 'w') as f:
        f.write(version)

def get_ver(version=None):
    if not getCfgVerFile().exists():
        write_ver(version or cfg.default_version)
        if not version:
            echo (f"Note: Using default version \'{cfg.default_version}\'")

    with open(getCfgVerFile(), 'r') as f:
        ver = f.read()

    if not ver in cfg.versions:
        fail (f"Version setting doesnt exist: {ver}", False)

    return ver

def get_ver_path(version, file):
    return getVerDir(version) / file

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
    try_bin_path = getDataDir() / "game.axf"
    try_exh_path = getDataDir() / "exh.bin"

    if not try_bin_path.exists():
        try_bin_path = getDataDir() / "code.bin"
        if not try_bin_path.exists():
            return None
        if not try_exh_path.exists():
            fail ("Found unsorted code.bin, but missing exh.bin. Please add exh.bin to data/ (exheader).", False)
    elif try_exh_path.exists():
        try_exh_path.unlink()

    # Check version
    version = get_file_ver(try_bin_path)
    if not version:
        echo ("Found loose data/code.bin, but does not correspond to any known version.")
        echo ("List of versions with SHA256:")
        for k, v in cfg.versions.items():
            print(k + ": " + v)

        fail ("Please verify your binaries, and try again.", False)

    # Move
    if not getVerDir(version).exists():
        getVerDir(version).mkdir(parents=True, exist_ok=True)

    if try_exh_path.exists(): # code.bin
        try_bin_path.rename(get_ver_path(version, "code.bin"))
        try_exh_path.rename(getHeadFile(version))
    else: # game.axf
        try_bin_path.rename(get_ver_path(version, "game.axf"))

    echo (f"Found loose binaries in data/, identified as v{version.upper()} and moved to data/ver/{version}/.")

    return version
