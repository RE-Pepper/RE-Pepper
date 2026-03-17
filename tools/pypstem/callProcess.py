#!/usr/bin/env python3
import subprocess
import os
import sys

from tools.low.glob import getCompilerPath, fail_ex, fail, echo

def _call(exe, arg_list, silent=False, capture=False):
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

    args = list(map(str, arg_list))

    if capture:
        ret = subprocess.run(args, env=env, capture_output=True, text=True)
    elif silent:
        ret = subprocess.run(args, env=env, stdout=subprocess.DEVNULL)
    else:
        ret = subprocess.run(args, env=env)

    if ret.returncode != 0:
        fail_ex (f"{path.name} failed with {ret.returncode}.", " ".join(map(str, arg_list)))

    return ret.stdout

def _get_bin(name):
    return getCompilerPath() / "bin" / f"{name}.exe"

def do_assemble(arg_list, silent=False, capture=False):
    return _call("armasm", arg_list, silent, capture)

def do_compile(arg_list, silent=False, capture=False):
    return _call("armcc", arg_list, silent, capture)

def do_link(arg_list, silent=False, capture=False):
    return _call("armlink", arg_list, silent, capture)

def do_archive(arg_list, silent=False, capture=False):
    return _call("armar", arg_list, silent, capture)

def do_export(arg_list, silent=False, capture=False):
    return _call("fromelf", arg_list, silent, capture)
