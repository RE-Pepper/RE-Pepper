# Forking this for another game

the tools don't care about 3D Land. armcc 4.x game? retail, dev, ARM,
Thumb -> it works.

## keep

```
make.py
tools/           (everything except splector)
data/template/   data/config.json   (structure, not values)
the map.csv format, it's the whole contract:

Start,Pool,End,Section,Rank,Type,Symbol,SectionName
```

## toss

```
data/ver/*        Game/  lib/  priv/  docs/
tools/splector/   (scrapped reassembly engine, unused)
```

## steps

1. `data/ver/<yourgame>/` -> code.bin + exh.bin
2. sha256 of the code.bin into `versions` (config.json or user config)
3. `python3 tools/pypstem/user/initMap.py <yourgame>` -> starter map
   (BL scan from the entry, ARM/Thumb auto detected)
4. `app_name` = first 6 bytes of your exh.bin, wire your modules
5. `python3 make.py <yourgame>`
6. `python3 tools/diff.py` -> should say MATCH. done.

## sdk headers

donor AXFs with DWARF (other games on the same SDK) give you types,
layouts, enum values, decl files and line numbers. rebuild the headers
from that. only provable facts go in, everything else stays unknown.

svc wrappers are free: literal translations of your binary's bytes.
