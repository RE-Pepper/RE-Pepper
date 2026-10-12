# Overview

RE-Pepper is a decomp with a matching linker: the build always outputs
a code.bin that's byte for byte identical to the original. Functions
you've decompiled get compiled from C++ and pinned to their original
addresses. Everything you haven't touched yet just uses the original
bytes. So the build never drifts, no matter how much or how little
you've done.

## The flow, roughly

```
map.csv  (addresses, ranks, section names — the source of truth)
   |
gen_original.py   cuts the image into units:
   |              pin   = a row whose compiled version exists
   |              slice = a run of original bytes (INCBIN, labeled)
   v
gen_scatter_match()   one LOAD region per unit, a ZI reservation so
   |                  Image$$ZI$$ZI$$Base/Limit exist, and a spill
   |                  region behind the image
   v
armlink   (official release flags + --remove)
   |
fromelf --bincombined   ->   code.bin  ==  original. always.
```

## How a row decides what it becomes

- The `.syms` cache (written during the build) lists every symbol that
  exists in compiled objects. Rows in there *can* pin.
- `data/ver/<ver>/.matchskip` lists rows that must NOT pin. It's
  self-healing: checkMatch --update adds rows whose bytes came out
  wrong, a failed link adds rows that didn't fit, and `--skip` adds
  one by hand. Rerun make.py and those rows go back to original bytes.
- A row with a SectionName owns the whole per-file data block — "one
  symbol includes all data from that file" — and absorbs the rows
  inside it. Rows without a SectionName pin per symbol.

## Why one load region per unit (the actual magic)

armlink packs stuff *inside* a load region sequentially. So if you put
all your units in one big region and one function comes out smaller
than its row, everything after it shifts and the whole diff explodes.
With one load region per unit, the load address equals the execution
address, and a bad pin can only damage its own row. You'll see it in
checkMatch as one wrong function, not a wall of red.

Retail-style sections (TEXT/RO/RW like a shipped build) are still
available if you want the .axf to look like a retail one — set
`retail_sections: true` — but only do that once every pin fills its
row exactly, or the shifting comes back.

## The tools

- `make.py` — build. Matching is the default (config `matching:true`).
- `tools/pypstem/` — the build system: check, split, build, link, export.
- `tools/low/` — helpers: unit decomposition, scatter generation,
  objdiff json, header/sym readers.
- `tools/3differ/` — the function differ. Capstone-based (no
  devkitPro needed), ARM and Thumb, normalizes branch targets, literal
  pool words and every image pointer to map symbols — so one fat
  function somewhere else doesn't zero your score. `watch.py` keeps
  itself open, rebuilds on save, ctrl+c leaves the final diff.
- `tools/checkMatch.py` — byte compare vs original + demote + spill.
- `tools/check.py` — rank updates (U/O/M/m) via 3differ.
- `tools/pypstem/user/initMap.py` — bootstrap a map.csv from a raw
  code.bin (BL scan + data pointer scan, ARM/Thumb auto).
- `modd-e-bug.py` (in your private 3ds/ collection, not the repo) —
  donor AXF DWARF analysis: `--short` dumps types with their original
  headers and line numbers, `--decl_file` rebuilds whole headers,
  `--lines --asm` shows a function's line table with inline resolution.

## State on disk

```
data/ver/<ver>/map.csv       the symbol map (source of truth)
data/ver/<ver>/.syms         symbols that exist in built objects
data/ver/<ver>/.matchskip    demoted rows (back to original bytes)
build/<ver>/split/original/  generated INCBIN slices + chunk files
build/<ver>/RE-Pepper.ld     generated scatter file
objdiff.json                 decomp.dev project file (auto-generated)
```
