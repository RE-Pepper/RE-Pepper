# Toolchain

the build tries to output a code.bin byte identical to the original.
decompiled code pins to its real address, everything else is original
bytes. the build can't drift.

## a map row becomes

- symbol in `.syms` -> pin (compiled code at the row's address)
- row in `.matchskip` -> slice (original bytes, never pins)
- row has a SectionName -> owns the whole per file data block
- everything else -> slice

bad pins -> demoted to `.matchskip` automatically, next build uses
original bytes again.

## the link

- one load region per unit -> a wrong pin only damages its own row
- retail style sections -> `retail_sections: true`, only when every pin
  fits exactly

## state on disk

```
data/ver/<v>/map.csv      the map, source of truth
data/ver/<v>/.syms        symbols in built objects
data/ver/<v>/.matchskip   demoted rows
data/ver/<v>/.demote_backlog.txt   last list of differing pins, todo
build/<v>/split/original/asm/orig_regions.s   linker region symbols
objdiff.json              decomp.dev file (generated)
```

## tools

- `make.py` -> build, matching is the default
- `tools/pypstem` -> the build system
- `tools/low` -> helpers: slices, scatter, objdiff
- `tools/diff.py` -> symbol differ
- `tools/diff.py --match` -> byte compare vs original
- `tools/check.py` -> update map ranks
- `user/initMap.py` -> bootstrap a map from a raw code.bin

see docs/armcc/Sti.md for static initializers (__sti, .init_array).
see docs/armcc/ for compiler quirks, SDK bugs, matching mechanics
and function-order identification. docs/rt-init.md covers the
SDK startup chain. docs/armcc/identify.md covers how the linker
decides function order and how to read it back into sources.
