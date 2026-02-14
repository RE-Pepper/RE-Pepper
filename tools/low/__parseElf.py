from io import StringIO
import subprocess
import sys
import os
import re
from _settings import *
from enum import IntEnum

class ElfFmt(IntEnum):
    Start = 0
    Size = 1

class ReadElfFmt(IntEnum):
    Index = 0 # Note: has a colon at the end
    Address = 1
    Size = 2
    Type = 3
    Scope = 4
    Visibility = 5
    Section = 6
    Symbol = 7

elf_exists = os.path.exists(getElfPath())
if elf_exists:
    # Step 1: Get Data
    cmd = f'"{Path(os.environ.get("DEVKITARM")) / "bin" / "arm-none-eabi-readelf"}" "{getElfPath()}" -sw -W'
    readelf_data = str(subprocess.check_output(cmd, shell=True))
    if sys.platform == 'win32': # Fix Newlines
        readelf_data = readelf_data.replace(r'\r\n', '\n')
    else:
        readelf_data = readelf_data.replace(r'\n', '\n')
    # Step 2: Filter Data
    lines = []
    for l in readelf_data.splitlines():
        a = l.split()
        if len(a) != (ReadElfFmt.Symbol+1): # Wrong number of cols
            continue
        if a[ReadElfFmt.Symbol] in ("$a", "$t", "$d", "$v0"):
            continue
        if a[ReadElfFmt.Symbol].startswith(("$a.", "$t.", "$d.")):
            continue
        if a[ReadElfFmt.Type] in ("FUNC","OBJECT","NOTYPE"):
            lines.append(l)
    readelf_data = "\n".join(lines)
    #print (readelf_data)

# TODO: remove once splector done
stubs_data = set()
with open(f"{getBuildPath()}/RedPepper.map") as f:
    s = StringIO(f.read())
    for line in s:
        if len(line.split()) == 6 and line.split()[5] == 'Stubs.o(stubs)':
            stubs_data.add(line.split()[0])

def get_elf_symbol(n):
    if not elf_exists or not n:
        return None
    if n in stubs_data:# TODO: remove once splector done
        return None
    s = StringIO(readelf_data)
    for l in s:
        a = l.split()
        if n == a[ReadElfFmt.Symbol]:
            return (int(a[ReadElfFmt.Address],16), int(a[ReadElfFmt.Size]))
    return None
