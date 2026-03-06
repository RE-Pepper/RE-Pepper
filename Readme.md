# RedPepper
 
This is a decompilation of Super Mario 3D Land (note that retail JP, KO, TW, and US versions are nearly identical).  
It is also fork from the repo on 3dsdecomp's github, and recieved some structural updates.  
Originally this is based on the EU release, but multiversion support is added and experimental.  
  
Check out the [docs](https://prp.moddi.dev)!

## Progress (EU)

<img src ="https://img.shields.io/endpoint?url=https://_github.moddi.dev/RedPepperDec/RedPepper/releases/download/stats-eu/Code.json&style=flat-square"/> <img src ="https://img.shields.io/endpoint?url=https://_github.moddi.dev/RedPepperDec/RedPepper/releases/download/stats-eu/Total.json&style=flat-square"/>

<img src ="https://img.shields.io/endpoint?url=https://_github.moddi.dev/RedPepperDec/RedPepper/releases/download/stats-eu/OK.json&style=flat-square"/> <img src ="https://img.shields.io/endpoint?url=https://_github.moddi.dev/RedPepperDec/RedPepper/releases/download/stats-eu/NonMatching.json&style=flat-square"/>

![Progress](https://github.com/RedPepperDec/RedPepper/releases/download/stats-eu/Progress.png)

## How To

As noted earlier, this fork made some updates regarding structure of some files.  
- code.bin goes to the data/ folder.  
- symbol files are gone, instead use the .csv files inside of the data/ folder.  
- cmake scrapped and wrote custom build system
- rebuild assembly (for possible modding support)

### Prequesites
    - Python 3
    - DevKitPro
    - `code.bin` and `exh.bin` extracted from Super Mario 3D Land

### Setup
- Clone this repository using ```git clone https://github.com/RedPepperDec/RedPepper.git```
- Enter directory, and clone submodules using ```git submodule update --init --recursive```
- Place the `code.bin` and `exh.bin` files in data/ver/{version}/code.bin
- Run 'python3 -m pip install colorama watchdog levenshtein cxxfilt pyelftools' to install python prequesites
- (Optional) If you want to run tools/progress.py, you also run 'python3 -m pip install GitPython matplotlib numpy'
- run ```py make.py {version}```. default version is EU


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

## SHASUM
(eu) ```code.bin: e1d7e188ff88467df776c17cec45c44857fadf5b699944baa8cddcae7d939e64```  
(eu_d) ```code.bin: 184b8804ccf4aea9f447b2278dfc3171d4f8c4e6abf890d7b24680d649e034c6```  
(jp) ```code.bin: 885dcaed5994076732b1f99e452a6f06493c23464ae0509ebbf44b8c6fd614a7```  
(jp_d) ```code.bin: b1987a589ddb9d4caf723e0dfb470131d2aee52023b8b9a90455f6c9f694fefc```  
(us_0) ```code.bin: c705711154b1c514d7a0b5d133fabff42834110b198bd4cf86397d0d1c1597e9```  
(us_1) ```code.bin: a38d213506f0477077c4a550f12dfd720e8c9bda00b7688c76b03360a538bb1a```  
(us_d) ```code.bin: 6016cbdada120b2476e512e8c87c5d525f62ee8daa9f81e00c8caa1237477344```  
(cn) ```code.bin: 11ca2f6fa7e8b9553737830899787e7236f4fdbf8b96ed03c99fbe6a8939b37d```  
(tw) ```code.bin: 6207415ee0c6d2dff53d65b39cc2b05318a3b25e62e39639ab2a7243d96357f0```  
(kr) ```code.bin: 820940dc19b86f8d47515973d9f1484c4efc0571a729c294e85b53e5097fda56``` 

## Links

- [Discord Server](https://discord.gg/wK4ZKa9QXq)
- [Old Wiki](https://al.littun.co/decomp)
- [decomp.me](https://decomp.me/preset/8)

## Credits
- [open-ead/sead](https://github.com/open-ead/sead)
- [original repo on 3dsdecump](https://github.com/3dsdecomp/RedPepper)
