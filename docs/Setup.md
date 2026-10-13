# Setup

## you need

- Python 3.10+
- `pip install colorama capstone pyelftools requests argcomplete watchdog python-Levenshtein cxxfilt GitPython matplotlib numpy mplcursors questionary`
- armcc 4.x under `data/compilers/` (which version goes where is in config.json)
- on linux: `wibo` at `data/compilers/wibo`

no env vars, no profile changes. the build handles the armcc env itself.

## commands

```
python3 make.py [version]                  build. matching is the default
python3 tools/diff.py                did it match? (add --update to demote)
python3 tools/3differ/diff.py eu <symbol>  diff a function
python3 tools/3differ/watch.py eu <symbol>  same, but popup + rebuilds on save
python3 tools/check.py                     update map ranks
```

the loop is: edit code, `make.py`, `diff.py`, repeat until MATCH.
when it says MATCH, your build is byte identical to the original.

`data/config.user.json` is your personal override file, it's gitignored.
