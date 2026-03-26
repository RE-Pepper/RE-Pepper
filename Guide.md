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
After that, the split system it started. it supports 2 modes:  
    - no split (default)  
    - yes split (--split)  
    If you dont split, it generates the stubs and dependency files so that the compiler can work with the functions.  
    If you do, the assembly will be split into many different files, and the build system will compile decompilation alongside split code.  
    Note that this is really slow, because the linker has to deal with a lot of sections. This cannot be avioded, as the functions need these separate sections.  
Next, the modules specified in the config are built. Here it does juggle around a bunch of settings, and build all sources it could find from a module.  
For each module, a library exists. It contains all the object files, and the linker can decide which functions to take in.  
If no modules exist, none will be built.  
Now before the linking step, the linker map and the json files (compile_commands, objdiff) are created.  
Lastly, it does link all the library files. Afterwards it does export a code.bin file from the build .axf file.  

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

