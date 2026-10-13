#!/usr/bin/env python3
from tools.pypstem._utils import *
from tools.pypstem.callProcess import do_link, do_link_soft
from tools.pypstem.manSetup import setup_compiler
from tools.low.glob import *
from tools.low.readSymMap import *
from tools.low.genScatter import gen_scatter, gen_scatter_match

ENTRY_SYM = "__ctr_start"

def exec_link():
    if cfg.matching:
        return exec_link_match()

    echo ("Generating ldscript")
    gen_scatter()

    echo ("Preparing to link ...", "\r")

    if getElfFile().exists():
        getElfFile().unlink()
    if getOutMapFile().exists():
        getOutMapFile().unlink()

    setup_compiler(cfg.compiler)

    flags = list(default_flags_link)
    flags.extend(cfg.flags_link)
    flags.append(f"--list={str(getOutMapFile())}")
    flags.append(f"--output={str(getElfFile())}")
    flags.append(f"--scatter={str(getOutScatterFile())}")

    depend_file = getSplitDependFile() or getBuildDependFile()
    if not depend_file:
        fail("No depend file found! (internal error)")
    flags.append(str(depend_file))

    flags.append(f"--userlibpath={str(getBuildLibPath())}")

    if not cfg.modules or len(cfg.modules) <= 0:
        pass # no libraries to search, matching mode works without any
    else:
        for mod_path_name, mod_data in cfg.modules.items():
            my_name = str(mod_data.get("name"))
            if my_name == getStubsLibName():
                continue
            if not (getBuildLibPath() / f"lib{my_name}.a").exists():
                continue # include only helper module, nothing built
            flags.append(f"--library={my_name}")

    if cfg.split:
        flags.append(f"--library={getSplitLibName()}")
    else:
        flags.append(f"--library={getStubsLibName()}")


    echo (f"Linking {getElfFile().name}")

    do_link (flags)

def _match_auto_demote(output):
    # parse linker errors that are clearly tied to pinned rows and
    # demote those rows to original bytes via the match skip list.
    # returns (demoted_names, other_error_lines)
    import re
    demoted = []
    other = []

    by_addr = {}
    for s in read_sym_file():
        if s[MapFmt.Symbol]:
            by_addr.setdefault(s[MapFmt.Start], []).append(s)

    pin_re = re.compile(r"ER_PIN_([0-9A-F]{8})")
    row_syms = {s[MapFmt.Symbol] for s in read_sym_file()}
    for line in output.splitlines():
        if "L6220E" in line:
            # execution region size exceeded: the compiled section is
            # bigger than the original row, it can never match
            m = pin_re.search(line)
            if m:
                addr = int(m.group(1), 16)
                for s in by_addr.get(addr, []):
                    if s[MapFmt.Symbol] not in demoted:
                        demoted.append(s[MapFmt.Symbol])
                continue
        if "L6218E" in line:
            m = re.search(r"Undefined symbol (\S+)", line)
            if not m:
                other.append(line)
                continue
            sym = m.group(1)
            if "depend.o" in line and sym in row_syms:
                # a pinned row was imported but nothing defines it anymore
                demoted.append(sym)
                continue
            if sym not in row_syms:
                # decompiled code references a symbol that has no map
                # row: demote the pins of the referring source file
                mobj = re.search(r"referred from (\S+)", line)
                if mobj:
                    stem = mobj.group(1).split("(")[-1].split("/")[-1]
                    stem = stem.rsplit(".", 1)[0]
                    import json
                    if getCfgSymsFile().exists():
                        try:
                            with open(getCfgSymsFile(), "r") as f:
                                syms_files = json.load(f)
                            for src, syms_list in syms_files.items():
                                if str(src).rsplit("/", 1)[-1].rsplit(".", 1)[0] == stem:
                                    for s in syms_list:
                                        if s in row_syms and s not in demoted:
                                            demoted.append(s)
                        except Exception:
                            pass
                continue
        if ("Error" in line or "Warning" in line) and line not in other:
            other.append(line)

    if demoted:
        f = getMatchSkipFile()
        existing = set()
        if f.exists():
            existing = {l.split("#")[0].strip() for l in f.read_text().splitlines()}
            existing.discard("")
        with open(f, "a") as fh:
            for name in demoted:
                if name not in existing:
                    fh.write(name + "\n")
                    existing.add(name)

    return demoted, other

def exec_link_match():
    # the build can rewrite .syms after exec_split decomposed, re-check
    # the slices so new symbols pin on the same run
    from tools.pypstem.stepSplit import assemble_orig, write_match_depend
    from tools.low.genOriginal import gen_original
    if gen_original():
        assemble_orig()
        write_match_depend()

    echo ("Generating matching ldscript")
    gen_scatter_match()

    echo ("Preparing to link ...", "\r")

    if getElfFile().exists():
        getElfFile().unlink()
    if getOutMapFile().exists():
        getOutMapFile().unlink()

    setup_compiler(cfg.compiler)

    # fresh list: never mutate the shared defaults
    flags = list(default_flags_link)

    # armlink validates that the entry points at real instructions, the
    # entry bytes come from an INCBIN slice so that cannot pass. the
    # ELF entry is irrelevant for code.bin anyway. only pass it when the
    # entry row is pinned from compiled code.
    from tools.low.genOriginal import build_units
    units, _header = build_units()
    entry_pinned = any(u.kind == "pin" and u.rows[0][MapFmt.Symbol] == ENTRY_SYM for u in units)
    if not entry_pinned:
        flags = [f for f in flags if not f.startswith("--entry=") and not f.startswith("--startup=")]

    flags.extend(cfg.flags_link)

    # official release link flags this build mirrors
    flags.append("--tailreorder") # official 3DS release flag, no-op with one section per region
    flags.append("--remove")       # drop unreferenced sections of pulled archive members

    flags.append(f"--list={str(getOutMapFile())}")
    flags.append(f"--output={str(getElfFile())}")
    flags.append(f"--scatter={str(getOutScatterFile())}")

    if not getBuildDependFile().exists():
        fail("No depend file found! (internal error)")
    flags.append(str(getBuildDependFile()))

    # original byte objects enter as direct objects, before the archives,
    # so their definitions win over archive members with the same name
    if not getOrigObjDir().exists():
        fail("Original byte objects are missing, run the split step. (internal error)")
    for obj in sorted(getOrigObjDir().glob("*.o")):
        flags.append(str(obj))

    flags.append(f"--userlibpath={str(getBuildLibPath())}")

    if not cfg.modules or len(cfg.modules) <= 0:
        pass # no libraries to search, matching mode works without any
    else:
        for mod_path_name, mod_data in cfg.modules.items():
            my_name = str(mod_data.get("name"))
            if my_name == getStubsLibName():
                continue
            if not (getBuildLibPath() / f"lib{my_name}.a").exists():
                continue # include only helper module, nothing built
            flags.append(f"--library={my_name}")

    # no stubs and no splector library in matching mode

    echo (f"Linking {getElfFile().name} (matching)")

    rc, output = do_link_soft(flags)

    if rc != 0:
        demoted, other = _match_auto_demote(output)

        echo (f"armlink returned {rc}, {len(output.splitlines())} output lines")
        for line in output.splitlines()[:40]:
            echo (line)
        for line in other[:30]:
            echo (line)
        if len(other) > 30:
            echo (f"... and {len(other) - 30} more messages")

        if demoted:
            for name in demoted:
                echo (f"Demoted to original bytes: {name}")
            echo ("The compiled version of these rows can not be placed, they")
            echo ("keep the original bytes now. Rerun make.py --match.")
            exit(1)

        fail_ex ("Linking failed.", "No pinned row could be auto demoted from the messages above.", False)
