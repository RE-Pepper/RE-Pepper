#!/usr/bin/env python3
import sys
def fail(msg: str):
    print(msg)
    sys.exit(1)

def typeToSection(type, name):
    if "g" in type: # any global def
        return "g."+name
    elif "ft" in type: # func template
        return "t."+name
    elif "f" in type: # fallback default func
        return "i."+name

    elif "dd" in type: #
        return ".data_"+name
    elif "dc" in type: # const data
        return ".constdata_"+name
    elif "db" in type: # bss data
        return ".bss_"+name
    elif "d" in type: # fallback default data
        return ".sdata_"+name

    elif not type:
        fail (f"Missing type for {name} at 0x{addr:08X}.")
    else:
        fail (f"Invalid type for {name} at 0x{addr:08X} : {type}")

def typeToSectionLinker(type, name):
    if "g" in type: # any global def
        return ":gdef:"+name
    else:
        return typeToSection(type, name)

