# Forking this thing for another game

None of the tools here care about Super Mario 3D Land specifically. If
your game was built with armcc 4.x, this works — retail, dev, ARM,
Thumb, whatever.

## What to toss

```
data/ver/*               (make a new folder for YOUR game instead)
data/config.user.json    (your personal registrations)
Game/  lib/              (all the decompiled game code)
docs/  Guide.md          (written for this project)
priv/                    (test scaffolding, a fake game used for testing)
tools/asm-differ/         (dead weight now, tools/3differ replaced it)
cmd.exe                  (only needed again if you link with wibo)
```

## What to keep

```
make.py
tools/pypstem/  tools/low/  tools/3differ/
tools/check.py  tools/checkMatch.py
data/template/  data/config.json   (the structure, not the values)
```

And the map.csv format — it's the whole contract between you and the
build system:

```
Start,Pool,End,Section,Rank,Type,Symbol,SectionName
```

## Getting your game running

1. Make `data/ver/yourgame/`, drop in your `code.bin` and `exh.bin`.

2. Add the game's sha256 to the `versions` dict in `data/config.json`
   (or just use `data/config.user.json` if you don't want to touch the
   main config).

3. Run `python3 tools/pypstem/user/initMap.py yourgame`

   This scans your code.bin from the entry point (following BL targets
   and data pointers) and spits out a starter map.csv of unnamed
   function rows. It auto-detects ARM vs Thumb, or force it with
   `--thumb`. You'll add names and data rows as you decompile.

4. Set `app_name` in the config (first 6 bytes of your exh.bin) and
   wire up your modules.

5. Build: `python3 make.py yourgame`
   Matching is the default (`"matching": true` in config.json).

6. Check: `python3 tools/checkMatch.py`
   It should say MATCH. If it does, your setup is done — everything
   in the build is original bytes, zero drift, zero risk.

## Rebuilding SDK headers (worth it, trust me)

If your game uses a known SDK (and whose 3DS game doesn't), you can
pull types, layouts, enum values and even the original line numbers
from donor AXFs that have DWARF — other games built on the same SDK.
Dump the structs/typedefs/enums with their decl files and lines, then
rebuild the headers in the original order. It feels like cheating but
it's all provable, which is the rule: only facts you can back up with
DWARF or with your own binary go into sources. Everything else stays
unknown until you can prove it.

Svc wrappers are the free part — they're literal translations of your
binary's bytes (swi number from the binary, section name from map.csv).
