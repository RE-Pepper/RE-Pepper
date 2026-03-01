#!/usr/bin/env python3
import os
from low.__manVer import get_ver
from pathlib import Path

def getProjDir(): # Resolve project path
    return Path(os.path.realpath(__file__).split("tools")[0].rstrip(os.sep))

def getVerDir(): # Get directory for version
    return Path(getProjDir()) / "data" / "ver" / get_ver()
def getMapFile(): # Map for all symbols
    return str(getVerDir() / "map.csv")
def getExeFile(): # Path of original code binary
    return str(getVerDir() / "code.bin")
def getHeadFile(): # Config for binary
    return str(next(getVerDir().glob("ex*.bin"), None))

def getBuildPath(): # Build path
    return str(Path(getProjDir()) / "build")
def getElfName(): # Name of built elf file
    return "RedPepper.axf"
def getElfPath(): # Path of build elf file
    return str(Path(getBuildPath()) / getElfName())

def getSplitPath(): # base dir for splits
    return Path(getVerDir()) / "split"

def getPresetId(): # Decomp.me PID for 3D Land
    return 8
def getAppName(): # Programm ID from exh.bin
    return b'CtrApp'
