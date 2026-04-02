#!/usr/bin/env python3
import sys

from tools.low.utilsPrint import *

def typeToSection(type, name):
    if "g" in type: # any global def
        return "g."+name
    elif "f" in type:
        if "t" in type: # func template
            return "t."+name
        else: # fallback default func
            return "i."+name

    if "dd" in type: # uhh data?
        return ".data_"+name
    elif "d" in type: # data.
        if "c" in type: # const data
            return ".constdata_"+name
        elif "b" in type and not "s" in type: # non-static bss data
            return ".bss_"+name
        else: # fallback default data
            return ".sdata_"+name

    if not type:
        fail (f"Missing type for {name}")
    else:
        fail (f"Invalid type for {name}: {type}")

def typeToSectionLinker(type, name):
    if "g" in type: # any global def
        return ":gdef:"+name
    else:
        return typeToSection(type, name)

