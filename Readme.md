# RE:Pepper
 
This is a reverse engineering project for Super Mario 3D Land.  
It is also fork from RedPepper on 3dsdecomp's github, massively upgrading the way it works.  
This decompilation targets the European version, but multiversion support was added and is experimental.  

> [!INFO]
> Current state of the project:
> Quite a few things were discovered, so I decided to reset the progress (for now). This means that I am moving individual files back into compilation, but checking and fixing some things.
  
> [!IMPORTANT]
> Reminder: **this will not produce a playable game.** This project will not allow you to play the game if you don't already own it.
  
> [!NOTE]
> This project was built in a way that allows for easy customization. If this were to be forked for another game, MIT License applies to the toolchain. The decompiled code is CC0.
  
Check out the [docs](https://prp.moddi.dev)!  
Chat about [3DS Decompilation](https://discord.gg/dFgw7CwrEX)!  
Ask in the [3DL Discord](https://discord.gg/wK4ZKa9QXq)!  

## Progress (EU)

<img src ="https://img.shields.io/endpoint?url=https://_github.moddi.dev/RE-Pepper/RE-Pepper/releases/download/stats-eu/Code.json&style=flat-square"/> <img src ="https://img.shields.io/endpoint?url=https://_github.moddi.dev/RedPepperDec/RedPepper/releases/download/stats-eu/Total.json&style=flat-square"/>

<img src ="https://img.shields.io/endpoint?url=https://_github.moddi.dev/RE-Pepper/RE-Pepper/releases/download/stats-eu/OK.json&style=flat-square"/> <img src ="https://img.shields.io/endpoint?url=https://_github.moddi.dev/RedPepperDec/RedPepper/releases/download/stats-eu/NonMatching.json&style=flat-square"/>

![Progress](https://github.com/RE-Pepper/RE-Pepper/releases/download/stats-eu/Progress.png)

## How To

As noted earlier, this fork of the RedPepper project made some updates:  
- symbol files are gone, instead use the .csv files inside of the data/ folder.  
- cmake scrapped and wrote custom build system along with new tools  
- code.bin and exh.bin go to the data/ folder.  
- rebuild assembly (for "possible" modding support)  

### Prequesites
    - Python 3
    - DevKitPro
    - `code.bin` and `exh.bin` extracted from Super Mario 3D Land

### Setup
#### Python
- To install all python dependencies at once, do `python3 -m pip install colorama capstone pyelftools requests argcomplete watchdog python-Levenshtein cxxfilt GitPython matplotlib numpy mplcursors questionary`
- If not, then for individuals:
  - Core: `capstone pyelftools requests`
  - asm-differ: `argcomplete watchdog python-Levenshtein cxxfilt`
  - progress.py: `GitPython matplotlib numpy mplcursors`
  - listsyms.py/upload.py: `cxxfilt` (optional)
  - upload.py: `requests questionary`

#### Project
- Clone this repository using ```git clone https://github.com/RE-Pepper/RE-Pepper.git```
- Enter directory, and clone submodules using ```git submodule update --init --recursive```
- Place the `code.bin` and `exh.bin` files in the data folder, the tools will put them where needed.
- run ```py make.py [version]```. default version is EU

> [!IMPORTANT]
> Note: **do not delete cmd.exe**, it is required to pass a silly check when building with armcc.

### Tools
The tools use python, and in the tools/ directory of this repository.  
For [...], run --help to get a list of options.

#### diff.py
```python tools/diff.py [asmdiff flags] <symbol>```
Start asm-differ, a cli interface to check the assembly of a function. 

#### upload.py
```python tools/upload.py <symbol>```
Upload a specific function to decomp.me

#### check.py
```python tools/check.py [...] [symbol]```
Check and update the csv function map.

#### listsyms.py
```python tools/listsyms.py [...]```
List symbols with different options.  

#### splector
Writes the assembly splits from the code.bin

#### pypstem
Core build system of the project

## SHASUM
note: retail JP, KO, TW, and US versions are nearly identical  
(eu) ```code.bin: e1d7e188ff88467df776c17cec45c44857fadf5b699944baa8cddcae7d939e64```   
(us) ```code.bin: a38d213506f0477077c4a550f12dfd720e8c9bda00b7688c76b03360a538bb1a```  
(jp) ```code.bin: 885dcaed5994076732b1f99e452a6f06493c23464ae0509ebbf44b8c6fd614a7```  
(eu_d) ```code.bin: 184b8804ccf4aea9f447b2278dfc3171d4f8c4e6abf890d7b24680d649e034c6```  
(jp_d) ```code.bin: b1987a589ddb9d4caf723e0dfb470131d2aee52023b8b9a90455f6c9f694fefc```  
(us_d) ```code.bin: 6016cbdada120b2476e512e8c87c5d525f62ee8daa9f81e00c8caa1237477344```  
(cn) ```code.bin: 11ca2f6fa7e8b9553737830899787e7236f4fdbf8b96ed03c99fbe6a8939b37d```  
(tw) ```code.bin: 6207415ee0c6d2dff53d65b39cc2b05318a3b25e62e39639ab2a7243d96357f0```  
(kr) ```code.bin: 820940dc19b86f8d47515973d9f1484c4efc0571a729c294e85b53e5097fda56``` 

## Links

- [Original Wiki](https://al.littun.co/decomp)
- [decomp.me](https://decomp.me/preset/8)

## Credits
- [open-ead/sead](https://github.com/open-ead/sead)
- [Original repo, RedPepper on 3dsdecomp](https://github.com/3dsdecomp/RedPepper)
