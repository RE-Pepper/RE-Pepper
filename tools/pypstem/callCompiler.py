#!/usr/bin/env python3
import subprocess
import os
import sys
from tools.low.glob import *
from tools.pypstem import manCompiler

def _call(path, args):
    cmd = []
    if isLinux():
        cmd.append("wibo")

    cmd.append(str(path))
    cmd.extend(args.split())

    env = os.environ.copy()
    env["TMP"] = "/tmp"
    env["TEMP"] = "/tmp"

    subprocess.run(cmd, env=env)

def do_assemble(path, flags):
    _call(str(path / "armasm.exe"), flags)

def do_compile(path, flags):
    echo (flags)
    _call(str(path / "armcc.exe"), flags)
