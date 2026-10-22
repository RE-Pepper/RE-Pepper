# armcc build quirks

behaviors verified against binaries or our own toolchain, not
from ARM PDFs. armcc 4.0 build 902 / armlink 4.1 build 791.

## section naming

- `--split_sections` puts each function in its own ELF section,
  named `i.<mangled_symbol>`. the scatter's pin regions select on
  exactly this name.
- `--remove_unneeded_entities` strips unreferenced statics and
  VFE-eliminated virtuals from the output.
- static data lives in `.data`, `.bss`, `.constdata.<base_file>`
  sections. the preinclude (`Game/project_globals.h`) forces ro/rw/zi
  section names per file with `_Pragma(arm section ...)`.

## what armcc refuses to do

- `#351`: the first parameter of any allocation function (operator
  new, custom overloads) must match the compiler's internal size_t,
  which is hardcoded `unsigned int` in build 902. `--diag_suppress`
  does not help. any header declaring `operator new(unsigned long)`
  will fail.
- armasm cannot define labels that collide with register names
  (r0-r15, a1-a4, v1-v8, sb, sl, fp, ip, sp, lr, pc). genOriginal
  warns and skips those labels. pipe-quoting `|name|` does not help.
- armasm symbol length limit: files rotate at ~240 labels to stay
  under the per-file area/label ceiling.

## mangling

- size_t in build 902 mangles as `j` (unsigned int, 4 bytes).
  the original game's toolchain used `m` (unsigned long), proven
  by `_Znwm` (operator new) and `tryCreateEm` in code.elf.
  the workaround is map alias rows, not header patches: you cannot
  make armcc 902 emit `m` without hitting `#351`.
- the `__sti___<len>_<stem>_cpp` length counts stem + "_cpp",
  not just the stem.

## vfe (virtual function elimination)

- armcc emits `.arm_vfe_header` sections in every TU.
- unreferenced virtuals get null slots in the vtable and their
  function bodies removed. proven: nw::lyt::Pane has null slots
  for Draw, LoadMtx, SetName, SetUserData in the game vtable
  while the decomp headers declare them as real virtuals.
- the consequence for matching: any compiled class with virtuals
  the original eliminated will have a different vtable and the
  pin fails on size. demote and move on.
- VFE only applies with `--arm_only` and `--no_exceptions`. most
  armcc targets compile for interworking (ARM + Thumb), which
  changes which virtuals are reachable and thus which get
  eliminated. redpepper builds with `--arm_only`.

## constant folding

- a constructor that only writes constants (no external calls,
  no vtable refs, no addresses) can be folded at compile time.
  the static's values bake into .data and no `__sti` is generated
  for the TU.
- not always: `-O3` with VFE kept the `__sti` in some test cases,
  but `--remove_unneeded_entities` can strip it if nothing
  references the static after folding.

## --remove on armlink

- armlink pulls the whole archive member when any symbol from it
  is referenced. `--remove` then drops unreferenced sections from
  the pulled member, but all remaining undefined symbols from all
  sections in that member must still resolve.
- this means one bad reference in one function of a pulled .o
  breaks the link for everything else in that .o.

## --tailreorder

- official 3DS release flag. reorders tail-calling sections into
  the caller's region. with the matching linker's per-unit load
  regions this should be a no-op (one section per region).
- it crashes armlink 4.1 build 791 with an internal fault when
  unplaced sections exist (demoted pins whose archive members are
  still pulled). keeping demoted members unpulled avoids the crash.

## --multibyte_chars / locale

- sources are shift-jis in the tree. `--multibyte_chars` with the
  default japanese locale reads them correctly.
- armcc cannot read a UTF-8 BOM (`\ufeff`) as shift-jis.
- if a shift-jis encode fails on a file that was already opened
  for writing, the file is truncated to zero. encode must happen
  before the file opens.
