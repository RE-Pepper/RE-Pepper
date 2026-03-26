#!/usr/bin/env python3

def echo(str, end="\n"):
    print (f"\033[38;5;221m{str}\033[0m\033[K", end=end)

def _fail_base(msg, det):
    if det: # backtrace
        raise RuntimeError(f"Failure!\n{msg}")
    else: # simple
        echo (msg)
        exit (1)
def fail(err, det=True):
    _fail_base(f"\033[38;5;196mError: {err}\033[0m\033[K", det)
def fail_ex(err, info, det=True):
    _fail_base(f"\033[38;5;196mError: {err}\033[0m\033[K\n\033[38;5;82m{info}\033[0m\033[K", det)

