# source layout identification

how to look at a flat code.bin and figure out what the original
source tree looked like: file names, folder structure, which TU
owns which function, and how the linker organized it all.

## symbols are sorted by mangled name within each archive

when armcc compiles a TU, every function gets a mangled symbol.
armlink stores archive members in the order they were given on
the command line, and the makefiles typically list files
alphabetically within each directory. so within one archive,
symbols cluster by their mangled prefix, which corresponds to
the class and then the file stem.

practical use: if you see `_ZN2al9LiveActor4killEv` next to
`_ZN2al9LiveActor6appearEv` in the binary, they are almost
certainly in the same TU. if the next symbol after them is
`_ZN2al9LiveActorFn6somethingEv` with a different length
prefix, that is a different class and likely a different file.

## the __sti list is a directory listing

every TU with a static constructor gets one `__sti___<len>_<stem>_cpp`.
the length prefixed stem is the file name without extension.
collecting all __stis from a binary gives you a complete list of
which files existed in the original build and had static
initializers.

more: the `.init_array` table order (see docs/Sti.md) tells you
which archive each __sti came from, because each alphabetical run
is one archive scan pass. consecutive __stis with stems from the
same subsystem (e.g. `seadHeapMgr_cpp`, `seadColor_cpp`,
`seadMatrix_cpp`) are from the same directory.

## non-virtual data: split by original folder path

static data symbols (globals, statics, vtables) carry the
mangled namespace and class name, but not the file path. the file
path shows up in the section name instead:

```
.constdata.<base_file_name>    read-only statics
.data.<base_file_name>         read-write statics
.bss.<base_file_name>         zero-init statics
```

armlink preserves these section names into the binary. in a
scatter map or fromelf dump, consecutive sections with the same
`<base_file_name>` belong to the same TU. files from the same
folder end up adjacent because the makefile passed them
together.

the preinclude in this project forces `arm section rodata=...`
etc to embed the base file name in the section name, which the
matching scatter then selects on.

## virtuals: dependency, not directory

virtual functions are a different story. the vtable
(referenced by any constructor or destructor) forces the linker
to resolve every virtual the class declares, whether or not
anything calls it. this pulls in archive members that the
directory ordering would not predict.

the `.init_array` order reflects this: the first entries are
what the crt chain references directly (core SDK, libc), then
each subsequent run is a deeper dependency wave. virtual-heavy
subsystems (nw::gfx, sead) pull their entire class hierarchy
early even if their source directory would sort later
alphabetically.

practical use: if a function appears in the binary between two
functions you know are from `seadHeap.cpp`, but its symbol
belongs to a different class, check if it is virtual. virtuals
get pulled when the vtable is emitted, which happens in the
first TU that constructs the class, not in the file that
declares them.

## the .ARM.exidx and .ARM.attributes

every function gets an `.ARM.exidx` entry (unwinding metadata,
needed for exceptions even with `--no_exceptions` for
debugging). these are LINKORDER-bound to their function's
section, so in a flat binary dump they appear right after the
function code.

`.ARM.attributes` sections carry build flags and ABI info per
TU. fromelf decodes these: they tell you which armcc build
compiled each TU, which CPU variant, which FP mode. if one
archive shows different attributes, it was built separately or
by a different toolchain version.

## practical recipe

```
1. dump all symbols from the binary (IDA or fromelf on the .elf)
2. collect all __sti___ names -> the file list
3. group non-__sti symbols by mangling prefix -> class clusters
4. within each cluster, look at .init_array order -> which
   archive, and within the archive, which directory
5. vtables tell you which virtuals exist and which were
   eliminated (null slots)
6. .ARM.attributes per TU -> toolchain version differences
7. .constdata/.data/.bss section names -> confirm file ownership
```

for a full reconstruction: the __sti list gives you every file,
the section names confirm the groupings, the .init_array order
gives you the directory hierarchy and the link order.
