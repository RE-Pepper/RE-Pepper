#!/usr/bin/env python3
import os
import sys

from pathlib import Path
from tools.low import cfg
from tools.low.utilsPrint import *

# scriptonly flags
g_is_silent = False # for functions that rewrite a line during output
g_version = None # game version global
g_compiler_path = None
g_compiler_ver = None

def setSilent():
    global g_is_silent
    g_is_silent = True
def setVersion(val):
    global g_version
    g_version = val
def setCompilerPath(path):
    global g_compiler_path
    g_compiler_path = Path(path)
def setCompilerVer(ver):
    global g_compiler_ver
    g_compiler_ver = str(ver)

def isLinux():
    return "linux" in sys.platform
def isSixFour():
    import platform
    return platform.machine().endswith('64')
def isSilent():
    return g_is_silent
def getVersion():
    return g_version or cfg.default_version or "invalid"
def getCompilerPath():
    return g_compiler_path
def getCompilerVer():
    return g_compiler_ver

# helpers
def getProjDir(): # Resolve project path
    import os
    return Path(os.path.realpath(__file__).split("tools")[0].rstrip(os.sep))

def getDataDir():
    return getProjDir() / "data"
def getVerDir(v=None): # Get directory for version
    return getDataDir() / "ver" / (v or getVersion())
def getStatsDir(): # Get Statistics directory
    return getDataDir() / "stats" / getVersion()
def getCompilersDir():
    return getDataDir() / "compilers"
def getCfgVerFile():
    return getProjDir() / "data" / ".version"
def getCfgMapFile(): # Path to map with date
    return getVerDir() / ".map"
def getCfgFlagsFile(): # List of all modules + flags
    return getVerDir() / ".flags"
def getCfgFlagsTFile(): # List of all modules + flags (temp)
    return getVerDir() / "..flags"
def getCfgSymsFile(): # List of all symbols + files
    return getVerDir() / ".syms"
def getMapFile(v=None): # Map for all symbols
    return getVerDir(v) / "map.csv"
def getHeadFile(): # Config for binary
    return next(getVerDir().glob("ex*.bin"), None)

def getBinAxfFile(v=None):
    return getVerDir(v) / "game.axf"
def getBinCodeFile(v=None):
    return getVerDir(v) / "code.bin"

def getBinFile(v=None):
    if getBinAxfFile(v).exists():
        return getBinAxfFile(v)
    else:
        return getBinCodeFile(v)

def isThumbVersion(v=None):
    return (v or getVersion()) in (cfg.thumb_versions or set())

def readBinImage(v=None):
    # the original image as flat bytes starting at the lowest load
    # address: code.bin passes through, an elf/axf original gets its
    # pt_load segments flattened. consumers index VA - text base, which
    # armlink 3ds images guarantee to be the lowest load address.
    data = getBinFile(v).read_bytes()
    if data[:4] != b"\x7fELF":
        return data
    import struct
    e_phoff = struct.unpack_from("<I", data, 0x1C)[0]
    e_phentsize, e_phnum = struct.unpack_from("<HH", data, 0x2A)
    segs = []
    lo = hi = None
    for i in range(e_phnum):
        off = e_phoff + i * e_phentsize
        p_type, p_offset, p_vaddr, p_paddr, p_filesz, p_memsz = struct.unpack_from("<IIIIII", data, off)
        if p_type != 1 or p_filesz == 0:
            continue
        segs.append((p_vaddr, data[p_offset:p_offset + p_filesz]))
        lo = p_vaddr if lo is None else min(lo, p_vaddr)
        hi = (p_vaddr + p_filesz) if hi is None else max(hi, p_vaddr + p_filesz)
    if not segs:
        return data
    out = bytearray(hi - lo)
    for vaddr, blob in segs:
        out[vaddr - lo: vaddr - lo + len(blob)] = blob
    return bytes(out)

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
def getBuildViaFile():
    return getBuildPath() / f"{cfg.project_name}.via"
def getBuildObjPath():
    return getBuildPath() / "obj"
def getBuildLibPath():
    return getBuildPath() / "lib"
def getBuildDependFile():
    return getSplitPath() / "depend.o"

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
# grabs symbols from libraries
def getSplitDependFile():
    return getSplitPath() / "depend.o"
# stubs
def getStubsLibName():
    return "stubs"
def getStubsLibFile():
    return getBuildLibPath() / f"lib{getStubsLibName()}.a"
def getStubsFile():
    return getSplitPath() / f"{getStubsLibName()}.c"
# original bytes (matching mode)
def getOrigDir(): # base dir for original byte slices
    return getSplitPath() / "original"
def getOrigAsmDir():
    return getOrigDir() / "asm"
def getOrigObjDir():
    return getOrigDir() / "obj"
def getMatchSkipFile(): # symbols matching mode must not pin (auto managed)
    return getVerDir() / ".matchskip"

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
# standalone tools (readHeader/readElfSym via fromelf) need a compiler
# path without the build setup; manSetup overrides it for the build
setCompilerPath(getProjDir() / "data" / "compilers" / str(cfg.compiler))

