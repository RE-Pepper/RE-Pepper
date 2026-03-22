#!/usr/bin/env python3
from tools.pypstem._utils import *
from tools.pypstem.callProcess import do_link
from tools.pypstem.manSetup import setup_compiler
from tools.low.glob import *
from tools.low.genScatter import gen_scatter

def exec_link():
    echo ("Generating ldscript")
    gen_scatter()

    echo ("Preparing to link ...", "\r")

    if getElfFile().exists():
        getElfFile().unlink()
    if getOutMapFile().exists():
        getOutMapFile().unlink()

    setup_compiler(cfg.compiler)

    flags = default_flags_link
    flags.extend(cfg.flags_link)
    flags.append(f"--list={str(getOutMapFile())}")
    flags.append(f"--output={str(getElfFile())}")
    flags.append(f"--scatter={str(getOutScatterFile())}")

    flags.append(str(getDependFile()))

    flags.append(f"--userlibpath={str(getBuildLibPath())}")

    if not cfg.modules or len(cfg.modules) <= 0:
        echo ("No modules are specified.")
    else:#replace with archive names
        for mod_path_name, mod_data in cfg.modules.items():
            my_name = str(mod_data.get("name"))
            flags.append(f"--library={my_name}")

    if cfg.do_split:
        flags.append(f"--library={getSplitLibName()}")

    echo (f"Linking {getElfFile().name}")

    do_link (flags)

