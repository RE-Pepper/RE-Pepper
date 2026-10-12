# Guide Collection
## Structure
### $v = Version, $p Project Name, $m Module Name
```
┌> build/  - Version-specific build folders
│ └─> $v/  - Build output
│ └> obj/  - Object files from build
│ │ └─> \*/  - Directory path from root folder
│ ├> lib/  - Library files from object files
│ │ └─> $m  - Library files that each include their modules object files
│ ├> split/  - Partly scrapped recompilation system's output
│ │ ├── depend.o/.s  - Depend file, listing functions to be pulled in
│ │ └── stubs.c  - nop stubs for all functions
│ ├> $p.axf  - Linked output from build
│ ├> $p.ld  - Linked map to force symbols to specific addresses
│ └> $p.map  - Text output from linker process
├> data/  - Directory for files to store for a bit longer
│ ├─ config.json  - Configuration file 
│ ├─ compilers/  - Folder where the compiler goes to
│ │ ├── 4.1/
│ │ │ └── 844/
│ │ └── wibo  - Light Linux-Windows bridge
│ ├─ stats/  - Output of tools/progress
│ │ └─> $v/  - Target specific files
│ │ ├── Code.json  - % value for matching bytes
│ │ ├── NonMatching.json  - Number of nonmatching functions
│ │ ├── OK.json  - Number of matching functions
│ │ ├── Progress.png  - Progress graph
│ │ └── Total.json  - Number of total functions
│ ├─ template/  - Templates
│ │ └── linker.ld  - Linker template
│ └─ ver/  - Version-specific target files
│    └─> $v/  - Target specific files
├> tools/  -
│ ├── check.py  - Check functions against map
│ ├── diff.py  - Display asm difference
│ ├── listsyms.py  - List symbols
│ ├── progress.py  - Calculate progress
│ ├── upload.py  - Create decomp.me scratch
│ ├── pypstem/  - Python Project System
│ ├── low/  - Small helper files
│ ├── splector/  - Scrapped reassembly engine
│ └── asm-differ/  - Backend for asm difference
├── cmd.exe  - KEEP THIS FILE, to make armcc work properly
├── compile_commands.json  - Generated for editors
├── diff_settings.py  - used by asm difference
├── Guide.md  - You Are Here
├── Readme.md  - Readme file
├── License  - License File
│
└── make.py  - Main Script
```

## General Idea
The python project system that was made for this project (pypstem) supports multiple versions.
When you call the script, it first builds the configuration.
It consists of three layers:
    1. data/config.json
    2. data/ver/$v/config.json
    3. data/config.user.json
If more than one were found, the one with the lower number does overwrite the settings.  
If a setting is a list, then it is added to. This includes modules.  
Then it tries to find the version by checking:  
    1. Loose binary (the script sorts this automatically)  
    2. Given input (parameter)  
    3. Previous version (data/.version)  
Once thats done, the default compiler (set in config.json) is being downloaded to ensure atleast one exists.  
After that, the split system it started. it supports 3 modes:  
    - no split (default)
    - yes split (--split)
    - matching (--match)
    If you dont split, it generates the stubs and dependency files so that the compiler can work with the functions.  
    If you do, the assembly will be split into many different files, and the build system will compile decompilation alongside split code.  
    Note that this is really slow, because the linker has to deal with a lot of sections. This cannot be avioded, as the functions need these separate sections.  
    If you match, every map row gets pinned to its original address (see Matching Linker below).  
Next, the modules specified in the config are built. Here it does juggle around a bunch of settings, and build all sources it could find from a module.  
For each module, a library exists. It contains all the object files, and the linker can decide which functions to take in.  
If no modules exist, none will be built.  
Now before the linking step, the linker map and the compile_commands json are created.  
Lastly, it does link all the library files. Afterwards it does export a code.bin file from the build .axf file.  
After a matching export, `objdiff.json` and the per-unit target objects in
`build/<version>/objdiff/` are generated for decomp.dev: one relocatable
`.o` per map row (original bytes, no base object = counts as zero progress),
plus a "mirror" object per decompiled source file (your compiled `.o`'s
structure with the original bytes swapped in, so objdiff shows whether your
source actually matches). objdiff can't diff whole executables, so the units
are real little objects. Nothing changed since the last run? The step skips
itself via a stamp.

## Matching Linker (--match)
`python3 make.py --match` builds a matching linker image: every function and
data object ends up at exactly the address it has in the original binary.
With `"matching": true` in data/config.json this is the **default**, a plain
`make.py` run builds it (use `--split` for the splector, or remove the config
key to get the old stubs build back).

How it works:
- The map rows are split into units. A row whose **compiled version exists**
  (its symbol is in the `.syms` build cache) is *pinned*: its section is
  selected into its own execution region at the row address, with the row
  size as maximum. A section that is even one byte bigger makes the link
  fail (region size exceeded), it can never silently shift other content.
  Everything else is covered by *slices*: contiguous runs of original
  `code.bin` bytes included byte for byte via armasm `INCBIN`, placed at the
  run start address. Named rows inside a slice get an `EXPORT` label at
  their exact offset, so decompiled code can reference them and raw
  branch/data references inside the slice stay valid.
- The scatter file mirrors the official CTR SDK region structure
  (`TEXT_SECTION`, `RO_SECTION`, `RW_SECTION` plus a `ZI` execution region so
  `Image$$ZI$$ZI$$Base/Limit` exist for crt0). Anything decompiled code adds
  that the original does not have (`.init_array`, `.ARM.exidx`, statics of
  pinned functions whose own rows are not pinned, ...) lands in `ER_SPILL`
  behind the last original byte. The link does not fail on it, but
  `tools/checkMatch.py` reports it.
- The link keeps the official release flags (`--inline`, `--largeregions`,
  `--pad=0xFF`, `--tailreorder`, plus `--remove`), so it behaves like the
  original build. `--keep=*` is not used, it would defeat the selection.
- The depend file imports one keep-alive symbol per slice and one symbol per
  pinned row, so exactly the pinned sections are pulled from the module
  archives. The original byte objects enter the link as direct objects
  before the archives, so their definitions win over same-named members.

**You never need to build without `--match`.** Pinning does not depend on
the map rank: any row with a compiled version is pinned, and rows that
turn out wrong demote themselves to original bytes:

- a pinned section bigger than its row fails the link with a region size
  error; `make.py --match` parses it, puts that row into
  `data/ver/$v/.matchskip` and tells you to rerun
- `python3 tools/checkMatch.py --update` byte compares the exported
  code.bin against the original and demotes every pinned row whose bytes
  differ (also into `.matchskip`)
- `python3 tools/checkMatch.py --skip <symbol|ER_PIN_xxxxxxxx>` demotes a
  single row by hand (use it when the link fails on a section that has no
  place in the original image, for example statics of a not fully
  decompiled TU)

So the iteration loop is: edit code, `make.py --match`,
`checkMatch.py --update`, rerun until it reports MATCH. The map rank
stays a pure progress indicator (`tools/check.py` still maintains it when
you want percentages); set `"only_matching": true` in the config to
restrict pinning to verified rank O rows instead.

Verify a build with `python3 tools/checkMatch.py`:
- byte compares the exported code.bin against the original (the RW page
  alignment padding at the end is re-added at export, like makerom does),
- attributes every differing byte range to map rows,
- checks that all pinned regions really sit at their addresses in the
  linker `.map`, and lists spill content.
Use `-v` for all offending rows, `-e` to exit non-zero when not matching.

Notes:
- armlink validates that the entry point is real code. While the entry
  bytes come from an original slice (armasm marks INCBIN as data) the
  matching link omits `--entry`/`--startup`; the 3DS loader uses the
  exheader entry anyway. They come back automatically as soon as
  `__ctr_start` is pinned from compiled code.
- `.syms` must reflect reality: if you disable modules, delete
  `data/ver/$v/.syms`, otherwise the build tries to pin rows whose objects
  no longer exist (the link auto demotes them, but it costs a rerun).
- because sections inside one execution region are sorted by attribute and
  then by name (DUI0474C 4.11), placement can only be controlled reliably
  with one region per symbol. Selector order in the scatter file is never
  placement order.
- armasm `INCBIN` resolves bare file names against the directory of the
  source file, and reports a missing file only as warning A1023E. The
  chunk files therefore sit next to the generated `.s` files and the
  assembler output is scanned, a missing chunk fails the build.
- armasm is a 32 bit tool and does not cope with one giant source: slices
  are split at word aligned label boundaries (max ~240 label points each)
  and the `.s` files rotate, so no file holds more than ~256 chunks. If
  armasm still fails on a file, lower ORIG_LABELS_MAX / ORIG_LABELS_PER_FILE
  in tools/low/genOriginal.py.

## Project Setup
This system was made with customizability in mind.  
For details on how it works, read the General Idea chapter above.
Note that --split was NOT tested with thumb code, and may break in that scenario.

### Map.csv
This file is a list of all symbols.  
**Start**: Address where this symbols starts  
**Pool\***: If function has a data pool, this is the start address of it.  
**End**: Total end of the function.  
**Section\***: If specified, groups functions together. only for last/next, not gaps.  
**Rank**: status of matching. O=Matching, M=Size Mismatch, m=Small Mismatch, U=Undefined  
**Type**: see Types below  
**Symbol\***: Name of the symbol. if empty, fn_x or dat_x is used (only when needed)  

### Types
- f: Function
   - (none): i.x
   - t: t.x template function
   - s: assembly function
- d: Data
   - (none): .sdata_x (custom section name to use with macro, to force section creation for local symbols)
   - g: :glob:x
   - c: .constdata_x data constant
   - d: .data_x
   - b: .bss_x

### Config.json
*all fields without a \* are required.*  

project_name:
 > Name used for the project (linker output, terminal..)  
 > default: None

app_name\*:
 > Name of the application from the exheader. Use this if you do not have an .axf file as target.  
 > default: None

decompme_id:
 > Id to pass to decompme when uploading a function  
 > default: None

versions:
 > a dictionary of versionname + sha256sum  
 > default: None

default_version:
 > name of the default version name  
 > default: None

compiler:
 > default compiler for the project  
 > default: None

modules\*:
 > List of all modules  
 > default: None

extensions\*:
 > list of file extensions (without dot)  
 > default: set(["cpp", "c", "s"])

flags_compile\*:
 > General compiler flags

flags_compile_cxx\*:
 > Additional flags to use when compiling C/C++ files

flags_compile_asm\*:
 > Additional flags to use when compiling ASM files

flags_link\*:
 > Linker flags

flag_preinclude\*:
 > relative path to the file that you wish every file to automatically include  
 > default: None

only_matching\*:
 > Switch to only allow matching functions to be in the linker file  
 > default: False

allow_shifting\*:
 > Switch to disable set addresses and allow for address shifting  
 > default: False

keep_objects\*:
 > Switch to stop deletion of built objects when they are not needed anymore  
 > default: True

macros\*:
 > Dictionary of macros  
 > default: False



## Tools quick reference

- `python3 tools/3differ/diff.py <ver> <symbol>` — function diff against
  the build. Branch targets, pool words and image pointers are normalized
  to map symbols, so shifted addresses do not poison the score.
  `--full` prints the whole function, `--color` forces colors.
- `python3 tools/3differ/watch.py <ver> <symbol>` — popup diff, watches
  sources, rebuilds on change, ctrl+c leaves the final state.
- `python3 tools/pypstem/user/initMap.py <ver>` — first map.csv from a
  raw code.bin (BL scan + data pointer scan, ARM/Thumb auto, --thumb to
  force). ~2/3 of the EU functions found this way.
- `python3 tools/check.py` — rank update (U/O/M/m) from the build, uses
  3differ, no devkitPro needed.
- donor AXF dwarf analysis (private 3ds/ tools): --short dumps types
  with original headers and lines, --decl_file rebuilds whole headers,
  --lines --asm shows per-function line tables with inline resolution.
