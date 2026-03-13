#!/usr/bin/env python3
import subprocess
import os
import sys

from tools.pypstem._utils import get_compiler
from tools.low.glob import fail_ex, fail, echo

def _call(path, arg_list):
    from tools.low.glob import isLinux

    idx = 0;
    if isLinux():
        arg_list.insert(idx, "wibo")
        idx += 1
    if not path.exists():
        fail_ex (f"Compiler binaries incomplete, cannot find {path.name}", f"At {path}")

    arg_list.insert(idx, str(path))

    env = os.environ.copy()
    env["TMP"] = "/tmp"

    ret = subprocess.run(arg_list, env=env)

    if ret.returncode != 0:
        fail_ex (f"{path.name} failed with {ret.returncode}.", f"{" ".join(arg_list)}")

def do_assemble(arg_list):
    _call(get_compiler() / "armasm.exe", arg_list)

def do_compile(arg_list):
    _call(get_compiler() / "armcc.exe", arg_list)

def do_link(arg_list):
    _call(get_compiler() / "armlink.exe", arg_list)

def do_archive(arg_list):
    _call(get_compiler() / "armar.exe", arg_list)

def do_export(arg_list):
    _call(get_compiler() / "fromelf.exe", arg_list)
