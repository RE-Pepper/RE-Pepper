#!/usr/bin/env python3
print ("Generating progress ...")

import datetime
import numpy
import io
import os
import sys
import json
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker
from time import sleep
from git import Repo
from pathlib import Path
from colorama import Fore

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from tools.low.readElfMap import *
from tools.low.readSymMap import *
from tools.low.readHeader import *

addr_base = read_header()[HeadType.Text][HeadVal.Start]

target_data = None
decomp_data = None
with open(getBinFile(), "rb") as f:
    data = f.read()
    target_data = memoryview(data)
with open(getExportFile(), "rb") as f:
    data = f.read()
    decomp_data = memoryview(data)

def writeHeader(ver: str, u: str, o: str, m: str, mm: str, total: str, bytes: str):
    textt = f"""## {ver.upper()} Matched: *{bytes}*

### Functions
**Match**: {o}
**Minor**: {mm}
**Major**: {m}
**Undefined**: {u}
**Total**: *{total}*
"""

    with open(getStatsDir() / "release.txt", 'w') as f:
        f.write(textt)

def getMatching(tg, tgs, dc, tcs):
    matching = 0
    size = min(tgs, tcs)

    for i in range(0, size, 4):
        if target_data[tg + i : tg + i + 4] == decomp_data[dc + i : dc + i + 4]:
            matching += 4

    return matching

def main():
    syms_undefined = 0
    syms_major = 0
    syms_minor = 0
    syms_ok = 0

    ver = getVersion()
    os.makedirs(str(Path('data') / 'stats' / ver), exist_ok=True)

<<<<<<< HEAD
    size_total = 0
    syms_total = 0
    matching = 0
    syms = read_sym_file()
    for sym in syms:
        rank = sym[MapFmt.Rank]
        size = sym[MapFmt.End] - sym[MapFmt.Start]
        name = sym[MapFmt.Symbol]
=======
    syms = read_sym_file()
    for sym in syms:
        if "b" in sym[MapFmt.Type] and "d" in sym[MapFmt.Type]:
            continue # skip bss
        syms_total += 1
>>>>>>> objdiff

        if name:
            sym_dec = get_elf_symbol(name, False)
            if sym_dec:
                dec_size = sym_dec[ElfMapFmt.Size]
                matching += getMatching(sym[MapFmt.Start] - addr_base, size, sym_dec[ElfMapFmt.Address] - addr_base, dec_size)

        syms_total += 1
        size_total += size

        match rank:
            case 'U':
                syms_undefined += 1
            case 'M':
                syms_major += 1
            case 'm':
                syms_minor += 1
            case 'O':
                syms_ok += 1

    def print_type(name: str, amount: str, number_color: Fore):
        print(name + ": " + (32 - len(name) - 2 ) * " " + number_color + amount + Fore.RESET)
    def write_type(rank: str, name: str, amount: str, color: str):
        out = {
            "label": name,
            "message": amount,
            "color": color,
            "schemaVersion": 1
        }
        with open(getStatsDir() / f"{rank}.json", 'w') as f:
            f.write(json.dumps(out))

<<<<<<< HEAD
    match_per = (matching / size_total * 100)
    matching_str = f"{match_per:.3f}% ({matching}b/{size_total}b)"
=======
    bytes_ok_str = f"{(bytes_ok / code_bin_size) * 100:.4f}% ({int(bytes_ok):,} bytes/{int(code_bin_size):,} bytes)"
>>>>>>> objdiff

    print_type("Total Functions", str(syms_total), Fore.LIGHTBLUE_EX);
    print_type("Matching", str(syms_ok), Fore.LIGHTGREEN_EX);
    print_type("Non-matching", str(syms_major + syms_minor), Fore.LIGHTYELLOW_EX);
    print_type("Functions match", matching_str, Fore.LIGHTCYAN_EX);

    write_type('Total', "Total Functions", str(syms_total), 'inactive');
    write_type('OK', "Matching", str(syms_ok), "success");
    write_type('NonMatching', "Non-matching", str(syms_major + syms_minor), "yellow");
    write_type('Code', "Functions match", matching_str, "informational");

    x_values = [datetime.datetime.now()]
    y_values = [(matching / size_total) * 100]

    numpy.seterr(all="ignore")
    repo = Repo(".")

    for commit in repo.iter_commits():
        file = None
        for path_parts in [
            ['data', 'Code.json'],
            ['data', 'stats', 'Code.json'],
            ['data', 'stats', ver, 'Code.json']
        ]:
            try:
                file = commit.tree
                for part in path_parts:
                    file = file / part
                break
            except KeyError:
                file = None
                continue
        if file is None:
            continue

        with io.BytesIO(file.data_stream.read()) as f:
            x_values.append(datetime.datetime.fromtimestamp(commit.committed_date))
            y_values.append(float(json.load(f)['message'].split('%')[0]))

    fig,ax = plt.subplots()

    dates = matplotlib.dates.date2num(x_values)
    ax.set_title(f"Progress for {ver.upper()}")
    ax.xaxis.set_major_formatter(matplotlib.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter())
    ax.plot(dates, y_values, '-')

    plt.savefig(getStatsDir() / "Progress.png")

    if 'show' in sys.argv:
        import mplcursors
        mplcursors.cursor(ax, hover=True)
        plt.show()

    writeHeader(ver, syms_undefined, syms_ok, syms_major, syms_minor, syms_total, matching_str)

if __name__ == "__main__":
    main()
