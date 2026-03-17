import os
import sys
from tools.low.glob import *

def apply(config, args):
    config["make_command"] = ["python", "make.py"]
    config["baseimg"] = str(getBinFile())
    config["myimg"] = str(getExportFile())
    config["source_directories"] = cfg.modules.keys()
    config["source_extensions"] = [".c", ".h", ".cpp", ".hpp"]
    config["arch"] = "armel"
    config["arch_objdump"] = "arm"
    config["objdump_executable"] = os.environ.get('DEVKITARM') + "/bin/arm-none-eabi-objdump"
