# the SDK init chain

how a retail 3ds binary starts up. the SDK's crt0 replaces the
compiler startup entirely: `__ctr_start` is the ELF entry and
runs the `nninit*` sequence. the compiler runtime only appears
where the SDK calls into it (`__rt_locale`, the `.init_array`
walker). verified from the game binary (names from `all.txt`,
disassembly of `code.bin`) and a debug donor `.axf` (DWARF:
`init/init_StartUp.cpp`, `init/init_Default.cpp`,
`crt0/MPCore/crt0.cpp`). dumped with `modd-e-bug.py --lines --asm`.

## the entry

`__ctr_start` (0x100000, armasm) is a fixed 9-slot chain:

```
1  bl nninitRegion                  0x100024
2  bl nninitLocale                  0x100190
3  bl nninitSystem                  0x29347C
4  bl nninitStartUp                 0x1007B4
5  bl __cpp_initialize__aeabi_      0x3A0DA4
6  bl nninitCallStaticInitializers  0x10015C
7  bl nninitSetup                   0x1001DC
8  bl nnMain                        0x100108
9  b  nn::svc::ExitProcess          0x293614
```

if `nnMain` returns, the process exits. a debug donor shows the
same skeleton; its slot 4 is a middleware override (`dslib`),
the game uses the SDK default. the donor sources name the
slots: `nninitRegion`/`nninitLocale` come from
`crt0/MPCore/crt0.cpp`, the rest from `init/init_StartUp.cpp`
and `init/init_Default.cpp`.

## slot by slot

**nninitRegion** - the SDK zeroes BSS itself, no
`__rt_stackinit`:

```
ldr r0, =Image$$ZI$$ZI$$Base      ; game: 0x3F39D8
ldr r1, =Image$$ZI$$ZI$$Limit     ; game: 0x431058
loop: strcc r2, [r0], #4          ; r2 = 0, word by word
```

**nninitLocale** - registers the SDK's crt0 globals
(`s_DebugIndicator`, `s_SdkVersion`, `s_FirmwareVersion`, all
in an anonymous namespace of crt0.cpp) via
`nnutilReferSymbol_`, then calls `__rt_locale` - the compiler's
locale pointer. this is the bridge: the SDK owns startup, the
C library owns locale.

**nninitSystem** - the SDK's `nn::os::Initialize` (donor: one
call; the game's body calls three sub-inits and tail-calls
deeper into the os cluster). placed far from the other nninit
functions (0x29347C vs 0x100xxx) by the call-depth sort, with a
4-byte nop pad in front of the body.

**nninitStartUp** - SDK 2.4 default: calls the `nninitSystem`
body again, then `nn::os::GetAppMemorySize` (0x100750) minus
`nn::os::GetUsingMemorySize` (0x100760) - the free memory size
in r0. the function ends `pop {r4, lr}` + nop and falls through
into the next section (0x1007D4), which consumes r0 (alignment
test, memory-region setup) and returns to `__ctr_start`. the
pair runs as one unit, r0 crosses the boundary.

**__cpp_initialize__aeabi_ (0x3A0DA4)** - the `.init_array`
walker, called directly from `__ctr_start`, NOT from
`__rt_entry` - there is no `_mainCRTStartup`/`__rt_entry` in a
retail 3ds link. ARM-only variant (`--arm_only`):

```
r4 = base  (pc relative literal)   ; game: 0x3A0DE4
r5 = limit (pc relative literal)   ; game: 0x3A1784
loop:
    r0 = [r4]
    lr = pc + 4                    ; return here (ARM state)
    r0 = r0 + r4                   ; target = entry + slot address
    mov pc, r0                     ; no blx, ARM only
    r4 += 4
    if r4 != r5 goto loop
```

the table: 616 self-relative entries, every word nonzero,
targets below the table. table mechanics, entry order and the
matching fingerprint: docs/armcc/Sti.md.

**nninitCallStaticInitializers** - the SDK's OWN static init
table, independent from `.init_array`:

```
r4 = Image$$STATIC_INIT$$RO$$Base
r5 = Image$$STATIC_INIT$$RO$$Limit
loop: r0 = [r4]; blx r0; r4 += 4   ; interwork-capable
```

in the game the range is empty (base == limit == 0x3E0E50, both
pool words identical), so the loop runs zero times. the donor
shows the same. a build could have the reverse (.init_array
empty, STATIC_INIT filled) - the two mechanisms never merge.

**nninitSetup** - four calls in source order (donor line
numbers 73-81, game shape matches):

```
nninitSetupDefault                ; game: 0x10109C
SetInternalErrorHandlingMode(false)
nn::applet::CTR::detail::Initialize(0)
nninitSetupDaemons                ; game: 0x1011BC
```

**nninitSetupDefault** (`init_Default.cpp`) -
`nn::srv::Initialize()`, `nn::srv::StartNotification()`,
`nn::os::ARM::detail::SaveThreadLocalRegionAddress()`.
**nninitSetupDaemons** - `nn::ndm::SetupDaemonsDefault()`.

**nnMain** - the game entry. the SDK calls the symbol `nnMain`,
not `main`.

## what the compiler runtime still does

- `__rt_locale` - called by nninitLocale
- `__cpp_initialize__aeabi_` - slot 5, walks `.init_array`
- heap/stack setup - not a compiler startup phase here; the OS
  owns memory, nninitStartUp only measures it

the stock armcc chain (`_mainCRTStartup`, `__rt_entry`,
`__rt_lib_init`, `__rt_stackheap_init`) does not run in a
retail 3ds binary; those symbols appear only if something
references them.

## why this matters for matching

- the 9 slots are fixed: a build whose crt0 differs in one slot
  diverges at the first `bl`.
- `.init_array` entry count and order are a full-link
  fingerprint (see docs/armcc/Sti.md).
- `nninitCallStaticInitializers` is a no-op with two identical
  pool words - a cheap check that the SDK table stayed empty.
- `nninitRegion`'s pool words are the BSS extent; they must
  match `Image$$ZI$$ZI$$Base/Limit` of the scatter.
