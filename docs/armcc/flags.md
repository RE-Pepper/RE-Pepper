# armcc and armlink options

from the official armcc 4.x docs (DUI0472C, DUI0474C) and the
toolchain itself. grouped by what they do. not all are used in
this build; the ones that are get a `*`.

## language mode

```
--c90               C mode (default for .c)
--c99               C99 mode
--cpp               C++ mode (default for .cpp)
--gnu              * GNU extensions, enables most GCC extensions
--strict            strict ISO mode
--strict_warnings   ISO warnings, still compiles
--anachronisms      allow old C++ features (pre-standard)
```

## code generation

```
--arm              * generate ARM instructions
--thumb             generate Thumb instructions
--apcs=/interwork    interworking calls (ARM<->Thumb)
--apcs=/nointer      no interworking
--arm_only          * (armlink only) no interworking veneers
--cpu=MPCore        * target the ARM11 MPCore (3DS)
--fpmode=fast       * fast VFP, no denormal/NaN checks
--fpmode=ieee_full   full IEEE 754 compliance
--fpmode=ieee_fixed  fixed-point
--fpmode=std         standard (default)
--signed_chars      * char is signed
--unsigned_chars     char is unsigned
--enum_is_int       * enums are 32-bit
--wchar16           * wchar_t is 16-bit
--wchar32            wchar_t is 32-bit
--dollar            * allow $ in identifiers
--multibyte_chars   * source is shift-jis
--locale=japanese     locale for multibyte (default from env)
--split_sections    * one ELF section per function
--split_ldm          split load/store multiples (avoid aborts)
--unaligned_access   allow unaligned word access
--narrow_volatile_bitfields  volatile bitfield packing
--min_array_alignment=opt  minimum array alignment
--pointer_alignment=num   pointer alignment
```

## optimization

```
-O0                  no optimization (reference builds)
-O1                  restricted optimization
-O2                  high optimization
-O3                 * maximum optimization
-Otime              * optimize for speed over size
-Ospace              optimize for size over speed
--forceinline       * force inline of every inline candidate
--autoinline         auto-inline small functions
--no_inline           disable all inlining
--vectorize          NEON auto-vectorization
--no_vectorize        disable NEON vectorization
--remove_unneeded_entities * strip unused statics and VFE virtuals
--data_reorder      * let armlink reorder data sections
--feedback=filename   use profile feedback for optimization
--ltcg               link-time code generation
--vfe               * virtual function elimination
--no_vfe             disable VFE
--multifile          compile multiple TUs as one (IPI)
```

the SDK uses either `-O3 -Otime` for release or `-O0` for
reference builds. nothing in between. the `-O0` builds with DWARF
are a primary reconstruction source for donor data.

## C++ features

```
--exceptions          enable exception handling
--no_exceptions      * disable exception handling
--exceptions_unwind   unwind tables even with --no_exceptions
--rtti                enable runtime type info
--no_rtti            * disable runtime type info
--no_rtti_data       * no RTTI data sections at all
--force_new_nothrow  * operator new returns null, adds throw()
--vla                allow variable-length arrays
--no_vla             * disable VLAs
--implicit_include    template instantiation from headers
--implicit_typename   implicit template parameter deduction
--friend_injection    friend declarations inject namespace
--guiding_decls       old-style guiding declarations
--pending_instantiations=n  limit template instantiations
```

## debug info

```
--debug               full DWARF debug info
--no_debug           * no debug info (release)
--debug_macros        macro debug info alongside code
--no_debug_macros    * strip macro debug info
--dwarf2              DWARF2 format
--dwarf3              DWARF3 format
--debug_info=line_inlining_extensions * inline origin tracking
--interleave          source + disassembly mixed output
-S                    assembly output only (used by this build)
```

## linker (armlink)

```
--scatter=file       * scatter file (memory layout definition)
--entry=address       ELF entry point
--userlibpath=dir    * library search path
--library=name       * link against lib<name>.a
--list=file          * output link map
--map                 show region sizes
--pad=0xFF           * fill padding with 0xFF
--tailreorder        * official 3DS release flag, moves tail
                       calling sections next to their target
--remove              drop unreferenced sections from pulled
                       archive members
--largeregions       * allow sections to span page boundaries
--no_list_mapping_symbols * suppress $a/$d/$t in map
--show_parent_lib    * show which archive each section came from
--sort=algorithm      section sort order
--first=section       place this section first in the region
--last=section        place this section last in the region
--zi_base=address     force ZI base address
--symbols             list all symbols
--xref                cross-reference listing
--callgraph           call graph analysis
--veneershare         share interworking veneers
--crosser_veneershare  share cross-region veneers
--info=totals         show section size totals
```

## diagnostics

```
--diag_style=gnu     * GCC-style diagnostic messages
--diag_suppress=tags  suppress specific warnings
--diag_warning=tags   make specific warnings errors
--diag_error=tags     make specific diagnostics fatal
--diag_remark=tags     make diagnostics into remarks
--remarks              show all remarks
--brief_diagnostics    short-form messages
--errors=file          redirect errors to file
--maxerrors=n          stop after N errors
--wrap_diagnostics     wrap long diagnostic text
```

## dependency and project

```
--preinclude=file    * header included before everything
--depend=file         output dependency file (.d)
--depend_format=unix_quoted * make-compatible .d format
--depend_system_headers * track system headers in .d
--no_depend_system_headers * don't track system headers
--md                  also generate .d during compile
--via=file            read additional options from file
--sys_include         treat #include <x> as system include
--kandr_include        old-style K&R include paths
--reduce_paths         remove redundant path components
--search_dynamic_libraries
```

## visibility and linking (ELF specific)

```
--hide_all             hide all symbols by default
--export_all_vtbl      export all vtables
--export_defs_implicitly
--dllexport_all        dll-export everything
--default_definition_visibility=level
```

## not used but exist

options the SDK could have used but didn't:

```
--bitband              bit-banding for Cortex-M
--arm_linux            ARM Linux specific paths
--ltcg                 link-time code generation
--profile              profiling support
--feedback             profile-guided optimization
--shared               build a shared library
--bpabi                Base Platform ABI
--datacompressor=opt   data section compression
```

## what this build uses

```
armcc: --arm_only --forceinline --split_sections --no_debug_macros
       -c -S --gnu --cpu=MPCore --fpmode=fast --apcs=/interwork
       -O3 -Otime --diag_style=gnu --signed_chars --dollar
       --multibyte_chars --enum_is_int --no_exceptions --no_rtti
       --no_rtti_data --remove_unneeded_entities --force_new_nothrow
       --signed_chars --wchar16 --no_vla --no_depend_system_headers
       --debug_info=line_inlining_extensions

armlink: --tailreorder --remove --cpu=MPCore --fpmode=fast
         --scatter=<file> --list=<file> --pad=0xFF
         --largeregions --no_list_mapping_symbols --show_parent_lib
```
