# Setup

## You need

- Python 3.10 or newer
- `pip install capstone pyelftools`
- ARM Compiler 4.x (armcc, armasm, armlink, fromelf, armar) — the tree
  expects them under `data/compilers/4.1/791` (and optionally `4.0/902`)
- On Linux: the `wibo` binary at `data/compilers/wibo` (it pretends to
  be Windows so armcc.exe doesn't have a meltdown)

That's it. No env vars, no shell profile changes — paths resolve from
the repo root and the build system sets the armcc env vars per module
on its own.

## The commands you'll actually use

```
python3 make.py [version]        build (matching is the default, always)
python3 make.py --clear_split    force-regenerate the original byte slices

python3 tools/checkMatch.py      "did it match?" + demotes bad pins
python3 tools/checkMatch.py --update   demote wrong pins, rerun after

python3 tools/3differ/diff.py eu <symbol>     diff one function
python3 tools/3differ/watch.py eu <symbol>    popup diff that watches
                                              your sources and rebuilds
                                              on save. ctrl+c leaves the
                                              final diff on screen.

python3 tools/check.py           update ranks (U/O/M/m) from the build

python3 tools/pypstem/user/initMap.py <ver>   bootstrap a map from code.bin
```

`data/config.user.json` is your personal overrides file (versions,
modules) — gitignored, use it for anything you don't want to commit.

## The daily loop

```
edit code -> make.py -> checkMatch.py -> repeat until MATCH
```

That's genuinely it. When checkMatch says MATCH, your build is byte
identical to the original, and every decompiled function you've added
is sitting at its real address doing its real thing.
