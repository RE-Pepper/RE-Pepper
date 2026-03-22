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
from tools.low.readSymMap import *

def write_release_txt(ver: str, u: str, o: str, m: str, mm: str, total: str, bytes: str):
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

def get_matching_bytes(orig: str, other: str):
    matching = 0
    with open(orig, 'rb') as orig_file:
        with open(other, 'rb') as other_file:
            while (b := orig_file.read(4)):
                if other_file.read(4) == b:
                    matching += 4
    return matching

def main():
    syms_undefined = 0
    syms_major = 0
    syms_minor = 0
    syms_ok = 0
    syms_total = 0
    bytes_ok = get_matching_bytes(getBinFile(), getExportFile())
    code_bin_size = os.path.getsize(getBinFile())
    ver = getVersion()
    os.makedirs(str(Path('data') / 'stats' / ver), exist_ok=True)
    
    syms = read_sym_file()
    for sym in syms:
        syms_total += 1

        match sym[MapFmt.Rank]:
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

    bytes_ok_str = "{:.4f}% ({:,} bytes/{:,} bytes)".format((bytes_ok / code_bin_size) * 100, int(bytes_ok), int(code_bin_size))

    print_type("Total Functions", str(syms_total), Fore.LIGHTBLUE_EX);
    print_type("Matching", str(syms_ok), Fore.LIGHTGREEN_EX);
    print_type("Non-matching", str(syms_major + syms_minor), Fore.LIGHTYELLOW_EX);
    print_type("code.bin", bytes_ok_str, Fore.LIGHTCYAN_EX);

    write_type('Total', "Total Functions", str(syms_total), 'inactive');
    write_type('OK', "Matching", str(syms_ok), "success");
    write_type('NonMatching', "Non-matching", str(syms_major + syms_minor), "yellow");
    write_type('Code', "code.bin", bytes_ok_str, "informational");

    x_values = [datetime.datetime.now()]
    y_values = [(bytes_ok / code_bin_size) * 100]

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

    write_release_txt(ver, syms_undefined, syms_ok, syms_major, syms_minor, syms_total, bytes_ok_str)

if __name__ == "__main__":
    main()
