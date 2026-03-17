#!/usr/bin/env python3
from os import path
from tools.low.glob import *
from tools.pypstem._utils import getFileBuildPath

# Generate compiler_commands.json

def gen_comcom():
    directory = str(getBuildObjPath())
    command = ""

    with open(getJsonComcomFile(), "w") as f:
        f.write("[")

        for src_path_name, src_data in cfg.modules.items():
            src_dir = src_data.get("source_dir") or "."
            src_path = getProjDir().joinpath(*str(src_path_name).split("/")).joinpath(*str(src_dir).split("/"))

            if str(getSplitAsmDir()) in str(src_path):
                continue

            for file in src_path.rglob("**.*"):
                output = path.relpath(getFileBuildPath(file), getBuildObjPath())

                f.write("\n{\n")
                f.write(f"  \"directory\": \"{directory}\",\n")
                f.write( "  \"command\": \"\",\n")
                f.write(f"  \"file\": \"{str(file)}\",\n")
                f.write(f"  \"output\": \"{str(output)}\"\n")
                f.write("},")

        f.seek(f.tell() - 1)
        f.truncate()
        f.write("\n]")
