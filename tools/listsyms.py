import sys
import argparse
try:
    import cxxfilt
    is_filter = True
except ImportError:
    is_filter = False
from _settings import *
from low.__parseElf import *
from low.__parseMap import *
from io import StringIO

def main():
    argbase = argparse.ArgumentParser(description="List Symbols")
    argbase.add_argument('-e', action='store_true', help='List compiled symbols instead of csv symbols')
    argbase.add_argument('-w', action='store_true', help='When using -e, only list symbols not in the csv')
    argbase.add_argument('-f', action='store_true', help='When using -w, list symbols that only mismatch in name')
    argbase.add_argument('-c', action='store_true', help='When using -e, compare address with csv, not compatible with -w')
    argbase.add_argument('-m', action='store_true', help='When using -e with -c, also only print non-matching')
    argbase.add_argument('-n', action='store_true', help='Only list names')
    argbase.add_argument('-a', action='store_true', help='Only list addr+name')
    argbase.add_argument('-A', action='store_true', help='Only list name+addr')
    argbase.add_argument('-R', action='store_true', help='When using one of the above, also list rank')
    argbase.add_argument('-d', action='store_true', help='Try demangling symbols (pip install cxxfilt)')
    argbase.add_argument('-s', action='store_true', help='Sort symbols alphabetically (mangled state)')
    argbase.add_argument('-i', action='store_true', help='Dont show special marker')
    argbase.add_argument('-zs', action='store_true', help='Show size as decimal')
    argbase.add_argument('-za', action='store_true', help='Show address as decimal')
    argbase.add_argument('-r', type=str, help='Only list symbols with specific ranking (O, m, M, U)')
    args = argbase.parse_args()

    has_found = False
    csv_names = []
    csv_syms = []
    if args.w:
        syms = read_sym_file()
        if args.f:
            csv_syms = syms
        for sym in syms:
            name=sym[MapFmt.Symbol]
            if not name or name is None:
                continue
            csv_names.append(name)

    if args.e:
        if args.c:
            print("elf / csv")
        for line in StringIO(readelf_data):
            sym = line.split()

            name = sym[ReadElfFmt.Symbol]
            addr = "0x{:08X}".format(int(sym[ReadElfFmt.Address], 16))
            size = "0x{:04X}".format(int(sym[ReadElfFmt.Size]))

            if not name or name is None:
                continue
            if args.w:
                if name in csv_names:
                    continue

            if args.zs:
                size = sym[ReadElfFmt.Size]
            if args.za:
                addr = int(sym[ReadElfFmt.Address], 16)
            if args.d and is_filter:
                try:
                    name = cxxfilt.demangle(sym[ReadElfFmt.Symbol])
                except cxxfilt.InvalidName:
                    name = sym[ReadElfFmt.Symbol]

            has_found = True

            csv_sym = get_symbol(sym[ReadElfFmt.Symbol])
            ex = ""
            if not args.w and ( csv_sym == None or csv_sym[MapFmt.Rank] != 'O' ):
                ex = " (U)"
            if args.w:
                if args.f:
                    csv_sym_try = get_symbol_with_addr_and_size(int(addr,16), int(size,16))
                    if (not csv_sym_try is None):
                        if (csv_sym_try[MapFmt.Symbol] != name):
                            print(f"{addr}:{size}: elf={name} != csv={csv_sym_try[MapFmt.Symbol]}")
                    continue
                print(f"{addr}: {name}")
                continue
            if args.c:
                if csv_sym == None:
                    continue
                csvaddr = csv_sym[MapFmt.Start]
                csvsize = csv_sym[MapFmt.End] - csv_sym[MapFmt.Start]
                if args.m:
                    if (int(csvaddr) == int(addr, 16)) and (int(csvsize) == int(size,16)):
                        continue
                if not args.za:
                    csvaddr = "0x{:08X}".format(csv_sym[0])
                if not args.zs:
                    csvsize = "0x{:04X}".format(csv_sym[2])
                print(f"{addr}:{size}/{csvaddr}:{csvsize}: {name}")
                continue
            if args.n:
                print(f"{name}{ex}")
                continue
            if args.a:
                print(f"{addr}:{size}: {name}{ex}")
                continue
            if args.A:
                print(f"{size}:{addr}: {name}{ex}")
                continue
                
            print(f"{addr}: {size}, {name}{ex}")
        return

    syms = read_sym_file()
    if args.s:
        syms.sort(key=lambda a: a[1])
    for sym in syms:
        addr = "0x{:08X}".format(sym[MapFmt.Start])
        size = "0x{:04X}".format(sym[MapFmt.End] - sym[MapFmt.Start])
        rank = sym[MapFmt.Rank]
        name = sym[MapFmt.Symbol]

        if not name or name is None:
            continue
        if not args.r is None:
            if rank != args.r:
                continue
        has_found = True

        if args.zs:
            size = sym[MapFmt.End] - sym[MapFmt.Start]
        if args.za:
            addr = sym[MapFmt.Start]
        if args.d and is_filter:
            try:
                name = cxxfilt.demangle(sym[MapFmt.Symbol])
            except cxxfilt.InvalidName:
                name = sym[MapFmt.Symbol]

        if args.n:
            if args.R and not args.r:
                print(f"{rank}: {name}")
            else:
                print(name)
            continue
        if args.a:
            if args.R and not args.r:
                print(f"{rank}: {addr}, {size}: {name}")
            else:
                print(f"{addr}: {size}: {name}")
            continue
        if args.A:
            if args.R and not args.r:
                print(f"{rank}: {size}, {addr}: {name}")
            else:
                print(f"{size}: {addr}: {name}")
            continue
            
        if sym[4] and not args.i:
            print(f"{addr}: {size},{rank},{sym[4]}: {name}")
        else:
            print(f"{addr}: {size},{rank}: {name}")
    if has_found == False:
        if (len(sys.argv) > 1):
            print ("No symbols found with specified settings.")
        else:
            print ("No symbols found.")

if __name__ == "__main__":
    main()
