#!/usr/bin/env python3
import subprocess
import os
import sys

from tools.low.glob import getCompilerPath, fail_ex, fail, echo

def _call(exe, arg_list):
    from tools.low.glob import isLinux

    path = _get_bin(exe)

    idx = 0;
    if isLinux():
        arg_list.insert(idx, "wibo")
        idx += 1
    if not path.exists():
        fail_ex (f"Compiler binaries incomplete, cannot find {path.name}", f"At {path}")

    arg_list.insert(idx, str(path))

    env = os.environ.copy()
    env["TMP"] = "/tmp"

    ret = subprocess.run(list(map(str, arg_list)), env=env)

    if ret.returncode != 0:
        fail_ex (f"{path.name} failed with {ret.returncode}.", " ".join(map(str, arg_list)))

def _get_bin(name):
    return getCompilerPath() / "bin" / f"{name}.exe"

def do_assemble(arg_list):
    _call("armasm", arg_list)

def do_compile(arg_list):
    _call("armcc", arg_list)

def do_link(arg_list):
    _call("armlink", arg_list)

def do_archive(arg_list):
    _call("armar", arg_list)

def do_export(arg_list):
    _call("fromelf", arg_list)
