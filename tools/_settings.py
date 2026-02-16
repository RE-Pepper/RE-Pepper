import os
from low.__manVer import get_ver
from pathlib import Path

def getProjDir(): # Resolve project path
    return Path(os.path.realpath(__file__).split("tools")[0].rstrip(os.sep))

def getMapFile(): # Map for all symbols
    return str(Path(getProjDir()) / "data" / "ver" / get_ver() / "map.csv")
def getExeFile(): # Path of original code binary
    return str(Path(getProjDir()) / "data" / "ver" / get_ver() / "code.bin")
def getConfFile(): # Config for binary
    return str(Path(getProjDir()) / "data" / "ver" / get_ver() / "config.txt")

def getBuildPath(): # Build path
    return str(Path(getProjDir()) / "build")
def getElfName(): # Name of built elf file
    return "RedPepper.axf"
def getElfPath(): # Path of build elf file
    return str(Path(getBuildPath()) / getElfName())

def getSplitPath(): # Output dir split
    return str(Path(getBuildPath()) / "split")
def getSplitAsmPath(): # asm output of split og
    return str(Path(getSplitPath()) / f"{get_ver()}.s")
def getSplitObjPath(): # as output of split og
    return str(Path(getSplitPath()) / f"{get_ver()}.o")

def getPresetId(): # Decomp.me PID for 3D Land
    return 8
