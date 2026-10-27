# source layout identification

how function order in the binary is decided, and how to read
the layout back into source structure. verified against the
armcc docs (DUI0472C, DUI0474C, DUI0475C, DUI0491C, DUI0493C),
controlled armlink experiments (RVCT 4.0 build 902) and six 3ds
game binaries.

## the placement pipeline

an address is decided in this order:

1. the scatter file picks the execution region (attribute
   selectors, `+FIRST`/`+LAST`).
2. within a region, sections group by attribute class
   (DUI0474C §"Section placement with the linker"):
   read-only code, read-only data, read-write code,
   read-write data, zero-init.
3. within one attribute class, the `--sort` algorithm orders
   the sections.
4. `--tailreorder` post-pass moves tail callers before their
   targets.
5. `--branchnop` (default on) replaces any branch whose target
   is now the next instruction with a NOP.
6. veneers are injected where a branch cannot reach.

the retail 3ds release link passes `--largeregions` and
`--tailreorder`. it never passes `--sort`, so the algorithm is
the large-region default: `AvgCallDepth` (DUI0493C §2.134.2).

## the sort algorithms

DUI0493C §2.134, abridged:

| algorithm | behavior |
|-----------|----------|
| Lexical | by section name, then input order on equal names |
| LexicalState | Thumb code before ARM code, then lexical |
| AvgCallDepth | Thumb before ARM, then approximated average call depth, ascending |
| RunningDepth | Thumb before ARM, then running depth: the depth of the callers, weighted by call count |
| CallTree | flattens the call tree into a list of read-only code sections, then appends all non-code sections lexically |
| BreadthFirstCallTree | CallTree with breadth-first flattening |
| ObjectCode | code sections by tiebreaker, everything else lexical |

default: `Lexical`. in large-region mode: `AvgCallDepth`.

note from the docs on AvgCallDepth: "the approximation of the
average call depth depends on the order of input sections" —
it is more input-order dependent than RunningDepth or CallTree.

## large-region mode

DUI0493C §2.76: large-region mode sorts by approximated
average call depth and may distribute veneers between the code
sections. the automatic switch happens when a region holds more
code than the smallest inter-section branch:

| branch range | condition |
|--------------|-----------|
| 32 MB | region contains only ARM code |
| 16 MB | Thumb code, Thumb-2 supported |
| 4 MB | Thumb code, no Thumb-2 |

`--no_largeregions` reverts to lexical order; DUI0474C §4.15:
without it, "section placement is then predictable".

measured (build 902): a ~200 byte region, far below every
threshold. four links of the same objects
(`main -> z -> y -> x` call chain):

| link flags | order | algorithm |
|------------|-------|-----------|
| none | x, y, z, main | lexical (default) |
| `--sort=Lexical` | x, y, z, main | lexical |
| `--largeregions` | main, z, y, x | AvgCallDepth |
| `--sort=AvgCallDepth` | main, z, y, x | AvgCallDepth |

explicit `--largeregions` forces the AvgCallDepth default —
the region size does not gate it. the game images are 2-8 MB of
ARM code and are not lexically ordered, consistent with
this. sorting all mangled names alphabetically and comparing
against the image order gives kendall tau 0.15-0.68 across six
donor binaries (1.0 would be lexical) — the order is not
lexical anywhere.

## what the call graph is

the linker approximates each section's call depth from the
branch relocations it resolves between sections. a function
called only through a pointer or a vtable has no static branch
edge, so it contributes nothing to its caller's depth. depth 0
is the entry side; deeper sections sit further along the call
chains. ascending depth order therefore puts callers before
callees, and whole call chains read front to back through the
image.

## ties

the sort needs a total order. measured at equal call depth:
the resolved order is section-name order (`i.<mangled>`)
ascending, in every tested configuration — object order on the
command line reversed, `--tiebreaker=cmdline` passed or not.

the documented tiebreaker (DUI0493C §2.154) is the creation
index by default: the order the linker creates input sections
in its internal structures; `--tiebreaker=cmdline` uses
command-line order (file.object.section) and is suggested for
use with `--scatter`. in practice the tiebreaker decides
same-named sections; different-named sections at equal depth
resolve by name.

## tailreorder

`--tailreorder` (DUI0493C §2.152) moves a tail-calling section
— one ending in a branch to the start of another section —
immediately before its target. restrictions:

- only one tail-calling section per target. with several, the
  one whose section name matches the target's moves; otherwise
  the first encountered.
- a tail caller never leaves its execution region.
- tail callers do not move before inline veneers.

measured: `u -> s` and `t -> s` tail calls, `main` calls both:

| link flags | order |
|------------|-------|
| none | s, t, u, main (lexical) |
| `--tailreorder` | t, s, u, main |
| `--largeregions --tailreorder` | main, t, s, u |

only `t` moved (first encountered); `u` stayed. after the move
`t`'s branch to `s` targets the next instruction, and
`--branchnop` (default on, DUI0493C §2.15) replaced it with a
NOP — the tail call became a fall-through.

under AvgCallDepth the caller usually sits before the callee
already, so tailreorder's visible effect is mostly on equal
depths and across cluster boundaries.

## veneers and mapping symbols

long branches that cannot reach get a veneer; in large-region
mode veneers are placed between code sections, controlled by
`--veneer_inject_type=individual|pool` (DUI0493C §2.161).
`individual` minimizes veneer count but "disrupts the structure
of the image the most".

mapping symbols in the final symtab: `$a`/`$t`/`$d` mark ARM
code, Thumb code, data (AAELF §4.6.5 table 4-6, DUI0474C §7.1:
"`$t` - start of a sequence of Thumb instructions"). the game
images keep almost none of these; what survives are `$v`
symbols — VFP related, emitted for armasm-written code
(DUI0474C §7.1). the 40-85 `$v0` symbols per image tag
hand-written assembly routines (entry stub, `nn::math::ARMv6::*`),
not veneers. the game is ARM only (`--arm_only`, no Thumb code
in the EU target), so the "Thumb before ARM" half of the sort
rule never reorders anything in practice.

donor images with Thumb code (stpl sdk 3.3/4.x: 144-157 `$t`
sites, all C library and `nn::prof`) also carry `$V` symbols —
the arm-to-thumb interworking veneer marker. every `$V` site
disassembles to `add ip, pc, #1; bx ip` (the canonical arm->
thumb stub), they appear only where thumb code exists, and the
letter is not in the arm pdfs — identified by disassembly. the
differ and modd-e-bug treat `$V` sites as arm code (the stub
body is arm).

## the mosaic the algorithm produces

the image is not one gradient. it is a mosaic:

- call chains read front to back: caller clusters before callee
  clusters, across module boundaries (library code interleaves
  with game code when they share chains).
- sections at equal depth keep name order — so every
  name-adjacent group with no call edges between them stays
  alphabetically sorted inside its slot.
- the `__sti` block sits at the end of code: `__sti...` sorts
  after every `_Z...` name, and the `__sti` functions have no
  code callers (`.init_array` data calls them), so they tie and
  fall to name order. measured in a donor binary: 441 of 441
  `__sti` functions in strict alphabetical order.
- library code interleaves with user code by depth: a test link
  placed `__user_initial_stackheap` between two user functions
  of adjacent depth.

measured across six donor binaries (category = top-level
namespace token; runs = stretches of one category):

| binary | funcs | runs | 1 func | 2-4 | 5-20 | >20 | largest run | __sti | thunks | templates | tau vs lexical |
|--------|-------|------|--------|-----|------|-----|-------------|-------|--------|-----------|----------------|
| EngineFinalROM | 15746 | 3005 | 1516 | 687 | 676 | 126 | 441 (sti block) | 441 | 42 | 23 | 0.68 |
| Bowling3DS | 3696 | 616 | 310 | 149 | 113 | 44 | 194 | 52 | 1 | 11 | 0.15 |
| SM2012 | 21117 | 4497 | 2428 | 1054 | 846 | 169 | 537 (sti block) | 537 | 80 | 93 | 0.52 |
| niconico | 105998 | 1728 | 583 | 449 | 361 | 335 | 6852 (template cluster) | 978 | 537 | 55333 | 0.50 |
| Boomerang | 9393 | 1349 | 770 | 326 | 170 | 83 | 574 | 577 | 129 | 463 | 0.45 |
| Musketeer | 7028 | 1243 | 707 | 324 | 147 | 65 | 461 | 464 | 35 | 363 | 0.37 |

60-83% of runs are 1-4 functions in every binary: single
functions and small groups of one namespace sit between other
namespaces' blocks. this interleaving is universal — toolchain
version, game size and genre do not change it.

## why classes cluster, why singletons happen

methods of one class call each other; along a chain depth
increases stepwise, so methods land at similar depths and the
name-order tie keeps them adjacent — a class block. the block
breaks where the call graph leaves the class: a method calling
into another module pulls that module's functions to a nearby
depth.

singletons are the same mechanism from the other side: a free
function or small helper called from many places has its depth
dictated by callers spread over the graph, so nothing else
shares its slot. namespace-level free functions (utility
helpers) are the most common singletons.

## the scatter file defines the region structure

the retail 3ds link uses this region structure:

```
TEXT_SECTION (code)
  STUP_ENTRY       __ctr_start +FIRST, then all +RO-CODE
  INIT_ARRAY       .init_array + init_aeabi.o

RO_SECTION (page-aligned)
  RO               all +RO-DATA
  STATIC_INIT      .static_init (empty in games)
  ET               .ARM.exidx, .ARM.extab

RW_SECTION (page-aligned)
  RW               all +RW-DATA
  ZI               all +ZI
```

`.init_array` sits inside TEXT_SECTION between the last code
and the page-aligned RO_SECTION — the table ends exactly at
text end. mechanics of the table and its self-relative
encoding: docs/armcc/Sti.md and docs/rt-init.md.

`+FIRST`/`+LAST` may not violate the attribute order
(DUI0474C): a `+LAST` selector cannot push read-only code
behind read-write data.

## the __sti list is a directory listing

every TU with a constructed static gets one
`__sti___<len>_<stem>_cpp`; the length counts stem + `_cpp`.
collecting them lists every file that had static initializers,
and their internal order is alphabetical — the name-order tie
at work.

## anonymous namespace reveals source file names

```
_GLOBAL__N__<len>_<filename>_cpp_<hash>
```

verified anon-ns TU counts: EngineFinalROM 8, Bowling3DS 10,
SM2012 11, Boomerang 11, Musketeer 12, niconico 170
(LiveWatchScene_cpp 280 functions, AppSettingScene_cpp 231,
CommentFilterWork_cpp 208). the count per TU says how much
file-static code that file had.

## data: section names carry the file

static data symbols carry the mangled namespace and class, not
the file. the file shows up in the section name:

```
.constdata.<base_file_name>    read-only statics
.data.<base_file_name>         read-write statics
.bss.<base_file_name>          zero-init statics
```

data sections are not call-depth sorted (the depth sort applies
to code), so data follows the attribute + name + position rules
inside its region.

## virtuals: vtables pull, not the directory

the vtable referenced by any constructor forces resolution of
every virtual the class declares, pulling archive members the
call graph alone would not reach. the vtable is emitted in the
first TU that constructs the class; a virtual can therefore sit
in the constructor's TU position rather than its declaration
file's.

VFE (`--vfe`, default on) removes unreferenced virtuals:
null slots in the vtable, bodies gone. proven: `nw::lyt::Pane`
has null slots for Draw/LoadMtx/SetName/SetUserData while the
decomp headers declare them live.

template instantiations and out-of-line inline copies are
COMDAT groups; the linker keeps one copy — the smallest by
default, the best debug view with `--bestdebug`
(DUI0493C, COMDAT selection). their placement is by the same
sort as any other code section, but their names derive from the
instantiation, not from a definition site (DUI0472C §8.35), so
they cluster by instantiation name: niconico carries 55333 of
them, mostly `__rw` and framework templates.

## practical recipe

```
1. dump symbols in address order (fromelf/objdump on the image)
2. __sti___ names      -> files with static initializers
3. _GLOBAL__N__ names  -> files with anon namespaces + sizes
4. group by mangled prefix -> class blocks (call clusters)
5. singletons          -> widely-called free functions/helpers
6. block boundaries    -> call-graph edges leaving the cluster
7. __sti internal order -> alphabetical; .init_array order ->
   link resolution waves
8. vtables             -> which virtuals exist; null slots = VFE
9. .constdata/.data/.bss section names -> file ownership
10. template name clusters -> which templates, used where
```

## what the function order tells you

1. primary: AvgCallDepth over the static call graph
   (`--largeregions` forces it).
2. ties: section name ascending.
3. secondary: `--tailreorder`, one tail caller per target.
4. `--branchnop` removes branches that became fall-throughs.
5. the approximation depends on input order — the same graph
   can lay out differently across toolchain builds.

consequences:

- adjacent functions usually share a call chain, not a file.
- a class block spans exactly the depths its methods occupy.
- file order cannot be recovered from function order alone;
  use symbol mangling, anon-ns names, section names and the
  __sti list for file structure.
- the __sti block is the one always-alphabetical region: it
  doubles as a checksum of the file list.
