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

    subprocess.run(cmd)

def do_assemble(path, flags):
    _call(str(path / "armasm.exe"), flags)

def do_compile(path, flags):
    _call(str(path / "armcc.exe"), flags)
