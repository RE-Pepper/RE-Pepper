#!/usr/bin/env python3
import os
import sys

from pathlib import Path
from tools.low import cfg

# scriptonly flags
is_silent = False # for functions that rewrite a line during output
version = cfg.default_version # game version global
compiler_path = None
compiler_ver = None

def setSilent():
    global is_silent
    is_silent = True
def setVersion(val):
    global version
    version = val
def setCompilerPath(path):
    global compiler_path
    compiler_path = Path(path)
def setCompilerVer(ver):
    global compiler_ver
    compiler_ver = str(ver)

def isLinux():
    return "linux" in sys.platform
def isSilent():
    return is_silent
def getVersion():
    return version or "eu"
def getCompilerPath():
    return compiler_path
def getCompilerVer():
    return compiler_ver

# helpers
def getProjDir(): # Resolve project path
    import os
    return Path(os.path.realpath(__file__).split("tools")[0].rstrip(os.sep))

def getDataDir():
    return getProjDir() / "data"
def getVerDir(): # Get directory for version
    return getDataDir() / "ver" / getVersion()
def getCompilersDir():
    return getDataDir() / "compilers"
def getCfgListFile(): # List of all src files + dates
    return getDataDir() / ".files"
def getCfgMapFile(): # Path to map with date
    return getDataDir() / ".map"
def getCfgFlagsFile(): # List of all modules + flags
    return getDataDir() / ".flags"
def getCfgFlagsTFile(): # List of all modules + flags (temp)
    return getDataDir() / "..flags"
def getCfgSymsFile(): # List of all symbols + files
    return getDataDir() / ".syms"
def getMapFile(): # Map for all symbols
    return getVerDir() / "map.csv"
def getBinFile(): # Path of original code binary
    return getVerDir() / "code.bin"
def getHeadFile(): # Config for binary
    return next(getVerDir().glob("ex*.bin"), None)

def getBuildPath(): # Build path
    return getProjDir() / "build" / getVersion()
def getElfName(): # Name of built elf file
    return f"{cfg.project_name}.axf"
def getElfFile(): # Path of build elf file
    return getBuildPath() / getElfName()
def getExportFile():
    return getBuildPath() / "code.bin"
def getOutScatterFile():
    return getBuildPath() / f"{cfg.project_name}.ld"
def getOutMapFile():
    return getBuildPath() / f"{cfg.project_name}.map"
def getOutCallFile():
    return getBuildPath() / f"{cfg.project_name}.txt"
def getBuildObjPath():
    return getBuildPath() / "obj"
def getBuildLibPath():
    return getBuildPath() / "lib"

def getJsonComcomFile():
    return getProjDir() / "compile_commands.json"
def getJsonObjdiffFile():
    return getProjDir() / "objdiff.json"

def getSplitPath(): # base dir for splits
    return getBuildPath() / "split"
def getSplitAsmDir():
    return getSplitPath() / "asm"
def getSplitObjDir():
    return getSplitPath() / "obj"
def getSplitLibName():
    return "splector"
def getSplitObjFile():
    return getSplitPath() / "splector.o"
def getSplitLibFile():
    return getBuildLibPath() / f"lib{getSplitLibName()}.a"
def getDependFile():
    return getSplitPath() / "depend.o"


# ui
def echo(str, end="\n"):
    print (f"\033[38;5;221m{str}\033[0m\033[K", end=end)
def _fail_base(msg, det):
    if det: # backtrace
        raise RuntimeError(f"Failure!\n{msg}")
    else: # simple
        echo (msg)
        exit (1)
def fail(err, det=True):
    _fail_base(f"\033[38;5;196mError: {err}\033[0m\033[K", det)
        
def fail_ex(err, info, det=True):
    _fail_base(f"\033[38;5;196mError: {err}\033[0m\033[K\n\033[38;5;82m{info}\033[0m\033[K", det)

# enable ansi colors on windows
if os.name == "nt":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
    mode = ctypes.c_uint()
    kernel32.GetConsoleMode(handle, ctypes.byref(mode))
    kernel32.SetConsoleMode(handle, mode.value | 0x0004)

# read config
cfg.read(getVerDir(), getDataDir())
setCompilerVer(cfg.compiler)

