#!/usr/bin/env python3
from pathlib import Path
from tools.low import cfg
from tools.low.__utilsVersion import get_ver

# helpers
def getProjDir(): # Resolve project path
    import os
    return Path(os.path.realpath(__file__).split("tools")[0].rstrip(os.sep))

def getDataDir():
    return Path(getProjDir()) / "data"
def getVerDir(): # Get directory for version
    return getDataDir() / "ver" / get_ver()
def getCompilerDir():
    return getDataDir() / "compilers"
def getListFile(): # List of all src files + dates
    return getDataDir() / ".list"
def getMapFile(): # Map for all symbols
    return getVerDir() / "map.csv"
def getBinFile(): # Path of original code binary
    return getVerDir() / "code.bin"
def getHeadFile(): # Config for binary
    return next(getVerDir().glob("ex*.bin"), None)

def getBuildPath(): # Build path
    return Path(getProjDir()) / "build"
def getElfName(): # Name of built elf file
    return f"{cfg.project_name}.axf"
def getElfFile(): # Path of build elf file
    return getBuildPath() / getElfName()
def getExportFile():
    return getBuildPath() / "code.bin"

def getSplitPath(): # base dir for splits
    return Path(getVerDir()) / "split"

def isLinux():
    import sys
    return "linux" in sys.platform

is_silent = False
def setSilent(): # for functions that rewrite a line during output
    global is_silent
    is_silent = True

# TODO: deprecate
def getPresetId(): # Decomp.me PID for 3D Land
    return cfg.decompme_id
def getAppName(): # Programm ID from exh.bin
    return cfg.app_name

# ui
def echo(str, end="\n"):
    print (f"\033[38;5;221m{str}\033[0m\033[K", end=end)
def _fail_base(err):
    print (f"\033[38;5;196mError: {err}\033[0m\033[K")
def fail(err):
    _fail_base(err)
    exit(1)
def fail_ex(err, info):
    _fail_base(err)
    print (f"\033[38;5;82m{info}\033[0m\033[K")
    exit(1)

# read config
cfg.read(getVerDir(), getDataDir())
