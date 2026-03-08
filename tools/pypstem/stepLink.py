#!/usr/bin/env python3
from tools.pypstem._utils import *
from tools.pypstem.callProcess import do_link
from tools.pypstem.manSetup import setup_compiler
from tools.low.glob import *
from tools.low.__genScatter import gen_scatter

def exec_link():
    echo ("Generating ldscript")
    gen_scatter()

    echo ("Preparing to link ...", "\r")

    set_compiler(setup_compiler(cfg.compiler))

    flags = cfg.flags_link
    flags += " --callgraph_output=text --callgraph_file="
    flags += str(getOutCallFile())
    flags += " --list="
    flags += str(getOutMapFile())
    flags += " --output="
    flags += str(getElfFile())
    flags += " --scatter="
    flags += str(getOutScatterFile())
    flags += " "

    flags += default_flags_link

    flags += " "
    flags += str(getDependFile())

    flags += " --userlibpath="
    flags += str(getBuildLibPath())
    flags += " "

    if not cfg.modules or len(cfg.modules) <= 0:
        echo ("No modules are specified.")
    else:#replace with archive names
        for mod_path_name, mod_data in cfg.modules.items():
            flags += " --library="
            flags += str(mod_data.get("name"))

    flags += " --library="
    flags += getSplitLibName()

    echo (f"Linking {getElfFile().name}")

    do_link (flags)

