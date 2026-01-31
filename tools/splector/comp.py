import os
import subprocess
from pathlib import Path
from _settings import *
from splector._utils import *

def execute(input, output):
    str(subprocess.check_output(f'"{Path(os.environ.get("DEVKITARM")) / "bin" / "arm-none-eabi-as"}" -mcpu=mpcore -mfpu=vfp -mfloat-abi=hard -o {output} {input}', shell=True))

def run():
    if not os.path.exists(getSplitOrigAsmPath()):
        print (f"{getSplitOrigAsmPath()} not found.")
        return

    execute(getSplitOrigAsmPath(), getSplitOrigObjPath())
