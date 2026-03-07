#!/usr/bin/env python3
from tools.pypstem.callProcess import do_export
from tools.pypstem._utils import *
from tools.low.glob import *

def exec_export():
    if not getElfFile().exists():
        exit(0)

    do_export(f"--bincombined {getElfFile()} --output {getExportFile()}")
