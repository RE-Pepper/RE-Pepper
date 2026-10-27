#!/usr/bin/env python3
# symbol differ forwarder. the engine lives in tools/3differ, the byte
# check in tools/3differ/match.py, the same way check.py goes through
# tools/low. flags: -m build first, -w watch, -3/-b three-way (need -w),
# -s stop at return, -B no arrows, -l skip lines, --full, --thumb/--arm
# force the isa, --color, --match (-q -v -e --update --skip SYM).

import sys
import argparse
import importlib
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from tools.low.glob import *
from tools.low.readSymMap import get_symbol, read_sym_file, MapFmt


def _differ():
    # tools.3differ starts with a digit, a plain import cannot name it
    return importlib.import_module("tools.3differ")


def _resolve_symbol(token):
    if token.startswith("0x"):
        addr = int(token, 0)
        for r in read_sym_file():
            if r[MapFmt.Start] == addr:
                return r
        return None
    return get_symbol(token)


def _make():
    import subprocess
    r = subprocess.run(
        [sys.executable, str(getProjDir() / "make.py"), getVersion()],
        capture_output=True, text=True,
    )
    return r.returncode == 0, (r.stdout or "") + (r.stderr or "")


def _elf_bytes():
    p = Path(getElfFile())
    return p.read_bytes() if p.exists() else None

def _snap_sources():
    # mtimes of every module source and the preinclude, os independent
    out = {}
    for mod_path_name, mod_data in cfg.modules.items():
        src_dir = mod_data.get("source_dir") or "."
        base = getProjDir().joinpath(*str(mod_path_name).split("/"))
        mod_src = base.joinpath(*str(src_dir).split("/"))
        if not mod_src.is_dir():
            continue
        for f in mod_src.rglob("*"):
            if f.is_file():
                try:
                    out[str(f)] = f.stat().st_mtime
                except OSError:
                    pass
    if cfg.flag_preinclude:
        p = getProjDir() / cfg.flag_preinclude
        if p.exists():
            out[str(p)] = p.stat().st_mtime
    return out


def _render(sym, thumb_hint, full, err, show_branches=True, stop_at_ret=0,
            base_bytes=None, prev_bytes=None, threeway=None):
    import shutil
    from tools.low.utilsPrint import echo
    differ = _differ()
    w, _ = shutil.get_terminal_size((100, 40))
    print("\033[2J\033[H", end="")
    echo (f"{cfg.project_name} v{getVersion().upper()}  {sym[MapFmt.Symbol] or hex(sym[MapFmt.Start])}")
    print("\u2500" * min(w, 100))
    if err:
        print("\033[31mbuild failed:\033[0m")
        for l in err.splitlines()[-12:]:
            print("  " + l)
        return None

    def section(label, data):
        echo (f"\u2500\u2500 {label} \u2500\u2500")
        print (differ.diff_symbol(sym, built_data=data, thumb_hint=thumb_hint, color=True,
                                  full=full, show_branches=show_branches,
                                  stop_at_ret=stop_at_ret).stdout)

    if threeway == "prev" and prev_bytes is not None:
        section("prev (before the last rebuild)", prev_bytes)
    if threeway == "base" and base_bytes is not None:
        section("base (when diff.py was started)", base_bytes)
    if threeway:
        echo ("\u2500\u2500 current \u2500\u2500")
    res = differ.diff_symbol(sym, thumb_hint=thumb_hint, color=True, full=full,
                             show_branches=show_branches, stop_at_ret=stop_at_ret)
    print(res.stdout)
    return res


def main():
    parser = argparse.ArgumentParser(description="3ds symbol differ")
    parser.add_argument("symbol", nargs="?", default=None, help="Map symbol name or 0xADDRESS")
    parser.add_argument("--version", metavar="VER", help="Version to diff (default: config default_version)")
    parser.add_argument("-m", "--make", action="store_true", help="Run make.py before diffing")
    parser.add_argument("-w", "--watch", action="store_true", help="Rebuild on source change and redraw")
    parser.add_argument("-l", "--skip-lines", metavar="LINES", type=int, default=0, help="Skip the first LINES lines of output")
    parser.add_argument("-s", "--stop-at-ret", dest="stop_at_ret", action="count", default=0, help="Stop the disassembly at the first return (-ss: second, ...)")
    parser.add_argument("-B", "--no-show-branches", dest="show_branches", action="store_false", help="Don't visualize branches")
    parser.add_argument("--full", action="store_true", help="Print the whole function, not only the diff")
    parser.add_argument("--thumb", action="store_const", const=True, dest="thumb_hint", help="Force thumb decoding")
    parser.add_argument("--arm", action="store_const", const=False, dest="thumb_hint", help="Force arm decoding")
    parser.add_argument("--color", action="store_true", help="Force colors")
    parser.add_argument("-3", "--threeway-prev", dest="threeway", action="store_const", const="prev",
                        help="Three-way: target, current, and the state before the last rebuild. Requires -w")
    parser.add_argument("-b", "--threeway-base", dest="threeway", action="store_const", const="base",
                        help="Three-way: target, current, and the state when diff.py was started. Requires -w")
    parser.add_argument("--match", action="store_true", help="Byte compare code.bin instead of diffing a symbol")
    parser.add_argument("-q", action="store_true", help="match mode: quiet, only summary")
    parser.add_argument("-v", action="store_true", help="match mode: verbose, list every bad row")
    parser.add_argument("-e", action="store_true", help="match mode: exit with error code when not matching")
    parser.add_argument("--update", action="store_true", help="match mode: demote pinned rows whose bytes differ into the skip list, then exit")
    parser.add_argument("--skip", metavar="SYM", help="match mode: demote a symbol (or ER_PIN_xxxxxxxx region name) by hand")
    args = parser.parse_args()

    if args.version:
        setVersion(args.version)

    if args.threeway and not args.watch:
        parser.error("-3/-b need -w")

    if args.match:
        margv = []
        if args.q: margv.append("-q")
        if args.v: margv.append("-v")
        if args.e: margv.append("-e")
        if args.update: margv.append("--update")
        if args.skip: margv += ["--skip", args.skip]
        importlib.import_module("tools.3differ.match").main(margv)
        return

    thumb_hint = args.thumb_hint
    sym = _resolve_symbol(args.symbol) if args.symbol else None
    if sym is None:
        from tools.low.utilsPrint import fail_ex
        fail_ex ("Symbol not found in map.", args.symbol or "", False)


    if args.watch:
        import time
        from tools.low.utilsPrint import echo
        err = None
        res = None
        base_bytes = _elf_bytes()
        prev_bytes = base_bytes
        try:
            prev_bytes = _elf_bytes() or prev_bytes
            ok, err = _make()
            res = _render(sym, thumb_hint, args.full, err if not ok else None,
                          show_branches=args.show_branches, stop_at_ret=args.stop_at_ret,
                          base_bytes=base_bytes, prev_bytes=prev_bytes, threeway=args.threeway)
            sources = _snap_sources()
            while True:
                time.sleep(1.0)
                now = _snap_sources()
                if now != sources:
                    prev_bytes = _elf_bytes() or prev_bytes
                    sources = now
                    ok, err = _make()
                    res = _render(sym, thumb_hint, args.full, err if not ok else None,
                                  show_branches=args.show_branches, stop_at_ret=args.stop_at_ret,
                                  base_bytes=base_bytes, prev_bytes=prev_bytes, threeway=args.threeway)
        except KeyboardInterrupt:
            pass
        if res is not None:
            echo ("final state:")
            print (res.stdout)
        return

    if args.make:
        ok, err = _make()
        if not ok:
            print("\033[31mbuild failed:\033[0m")
            for l in err.splitlines()[-12:]:
                print("  " + l)
            sys.exit(1)

    differ = _differ()
    res = differ.diff_symbol(sym, thumb_hint=thumb_hint,
                             color=True if args.color else None, full=args.full,
                             show_branches=args.show_branches, stop_at_ret=args.stop_at_ret)
    out = res.stdout.splitlines()
    if args.skip_lines:
        out = out[args.skip_lines:]
    print ("\n".join(out))
    sys.exit(res.returncode)


if __name__ == "__main__":
    main()
