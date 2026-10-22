# matching linker mechanics

how the matching build places code, resolves symbols and stays
byte-identical. this covers the armlink interaction, not the
python tooling (see docs/Overview.md for that).

## pin vs slice

a map row becomes:
- a **pin** when the symbol exists in `.syms` (compiled) and is not
  in `.matchskip`. armlink places the compiled section at the
  row's start address in a dedicated load region.
- a **slice** otherwise: the original code.bin bytes, INCBIN'd,
  with a label for the row's symbol if it has one.

bad pins (bytes differ from the original) are demoted to
`.matchskip` by `tools/diff.py --update` or the build's auto
demote. the next build uses original bytes for them.

## one load region per unit

the scatter gives every unit (pin or slice) its own `LR_*` /
`ER_*` pair at the exact original address. this means:

- a wrong pin only damages its own row, not its neighbors
- there is no code movement, no layout drift
- the output is byte-for-byte the original, or it is MISMATCH

## spill

sections from compiled objects that don't get placed (the object
was pulled for one symbol, its other sections have no region) go
to a spill region past the original image end. the export trims
them.

spill sections are only a problem when `--tailreorder` is active:
armlink 4.1 build 791 crashes with an internal fault if it tries
to reorder a tail call into a region that doesn't exist.

## original byte objects come first

the `orig_*.o` files (INCBIN'd original bytes with labels) are
passed to armlink as direct objects before the archives. when both
an original object and a compiled archive member define the same
symbol, armlink takes the first one it sees. this is why a demoted
row's original bytes always win over the still-compiled archive
version.

## the RW page padding

fromelf exports the last loadable byte, which is the RW end. the
original code.bin carries the makerom page padding after that:
all zeros, from RW end to the file end. the spill's sections land
in the same page, so the export zeroes everything past the RW
end.

## linker region symbols

the original crt code references linker-generated symbols:

```
Image$$STATIC_INIT$$RO$$Base / Limit   (used by init_StartUp.cpp)
Load$$LR$$TEXT_SECTION$$Base / Length   (used by os_Memory.cpp)
```

armlink generates these only when a scatter region has the
matching name. the matching scatter doesn't name regions
`TEXT_SECTION` or `STATIC_INIT`, so they are emitted as absolute
symbols in `orig_regions.s`:

- `STATIC_INIT` points to the RO end (empty range)
- `TEXT_SECTION` spans the whole load image: Base = text start,
  Length = RW end minus text start

## depend.o

the split step generates a `depend.o` containing the original
bytes for one unit. it references map symbols the same way
compiled code does. when a referenced symbol has no definition
(e.g. it was never compiled and has no map row), armlink reports
it as undefined. adding a map row for the address fixes it: the
slice then exports the label and depend.o resolves against it.
