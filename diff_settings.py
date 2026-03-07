import os
import sys
from tools.low.glob import getBinFile, getExportFile

def apply(config, args):
    config["make_command"] = ["python3", "make.py"]
    config["baseimg"] = getBinFile()
    config["myimg"] = getExportFile()
    config["source_directories"] = ["Game", "lib"]
    config["source_extensions"] = [".c", ".h", ".cpp", ".hpp"]
    config["arch"] = "armel"
    config["arch_objdump"] = "arm"
    config["objdump_executable"] = os.environ.get('DEVKITARM') + "/bin/arm-none-eabi-objdump"
