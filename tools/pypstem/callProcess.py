#!/usr/bin/env python3
import subprocess
import os
import sys

from tools.low.glob import getProjDir, getCompilerPath, getCompilersDir, fail_ex, fail, echo

def _call(exe, arg_list, silent=False, capture=False):
    from tools.low.glob import isLinux
    path = _get_bin(exe)

    idx = 0;
    if isLinux():
        # Create cmd.exe in root directory, workaround for armcc
        open(getProjDir() / "cmd.exe", 'a').close()
        # prepend wibo in command for wibo wrapper
        arg_list.insert(idx, str(getCompilersDir() / "wibo"))
        idx += 1
    if not path.exists():
        fail_ex (f"Compiler binaries incomplete, cannot find {path.name}", f"At {path}")

    arg_list.insert(idx, str(path))

    env = os.environ.copy()
    env["TMP"] = "/tmp"

    args = list(map(str, arg_list))
    #print(args)

    if capture:
        ret = subprocess.run(args, env=env, capture_output=True, text=True)
    elif silent:
        ret = subprocess.run(args, env=env, stdout=subprocess.DEVNULL)
    else:
        ret = subprocess.run(args, env=env)

    if ret.returncode != 0:
        if capture:
            # the caller wanted the output, but on failure it would be
            # lost. show what the tool actually said before failing.
            out = ((ret.stdout or "") + (ret.stderr or "")).splitlines()
            for line in out[:40]:
                echo (line)
            if len(out) > 40:
                echo (f"... and {len(out) - 40} more lines (rerun the shown command by hand to see all)")
        fail_ex (f"{path.name} failed with {ret.returncode}.", " ".join(map(str, arg_list)), False)

    return ret.stdout

def _get_bin(name):
    return getCompilerPath() / "bin" / f"{name}.exe"

def do_assemble(arg_list, silent=False, capture=False):
    return _call("armasm", arg_list, silent, capture)

def do_compile(arg_list, silent=False, capture=False):
    return _call("armcc", arg_list, silent, capture)

def do_link(arg_list, silent=False, capture=False):
    return _call("armlink", arg_list, silent, capture)

def do_link_soft(arg_list):
    # links without failing: returns (returncode, combined_output).
    # used by matching mode to inspect linker errors and auto demote
    # offending pinned rows instead of dumping a raw failure.
    import subprocess
    from tools.low.glob import isLinux
    path = _get_bin("armlink")

    args = []
    if isLinux():
        open(getProjDir() / "cmd.exe", 'a').close()
        args.append(str(getCompilersDir() / "wibo"))
    if not path.exists():
        fail_ex (f"Compiler binaries incomplete, cannot find {path.name}", f"At {path}")
    args.append(str(path))
    args.extend(map(str, arg_list))

    env = os.environ.copy()
    env["TMP"] = "/tmp"

    ret = subprocess.run(args, env=env, capture_output=True, text=True)
    return ret.returncode, (ret.stdout or "") + (ret.stderr or "")

def do_archive(arg_list, silent=False, capture=False):
    return _call("armar", arg_list, silent, capture)

def do_export(arg_list, silent=False, capture=False):
    return _call("fromelf", arg_list, silent, capture)
