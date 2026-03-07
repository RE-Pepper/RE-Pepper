#!/usr/bin/env python3
import subprocess
import os
import sys

from tools.pypstem._utils import get_compiler
from tools.low.glob import fail_ex

def _call(path, arg):
    from tools.low.glob import isLinux

    cmd = []
    if isLinux():
        cmd.append("wibo")
    if not path.exists():
        fail_ex (f"Compiler binaries incomplete, cannot find {path.name}", f"At {path}")

    cmd.append(str(path))
    cmd.extend(arg.split())

    env = os.environ.copy()
    env["TMP"] = "/tmp"

    subprocess.run(cmd, env=env)

def do_assemble(arg):
    _call(get_compiler() / "armasm.exe", arg)

def do_compile(arg):
    _call(get_compiler() / "armcc.exe", arg)

def do_link(arg):
    _call(get_compiler() / "armlink.exe", arg)

def do_export(arg):
    _call(get_compiler() / "fromelf.exe", arg)
