#!/usr/bin/env python3
import os
from pathlib import Path

versions = {
    "cn": "11ca2f6fa7e8b9553737830899787e7236f4fdbf8b96ed03c99fbe6a8939b37d",
    "eu": "e1d7e188ff88467df776c17cec45c44857fadf5b699944baa8cddcae7d939e64",
    "eu_d": "184b8804ccf4aea9f447b2278dfc3171d4f8c4e6abf890d7b24680d649e034c6",
    "jp": "885dcaed5994076732b1f99e452a6f06493c23464ae0509ebbf44b8c6fd614a7",
    "jp_d": "b1987a589ddb9d4caf723e0dfb470131d2aee52023b8b9a90455f6c9f694fefc",
    "kr": "820940dc19b86f8d47515973d9f1484c4efc0571a729c294e85b53e5097fda56",
    "tw": "6207415ee0c6d2dff53d65b39cc2b05318a3b25e62e39639ab2a7243d96357f0",
    "us_0": "a38d213506f0477077c4a550f12dfd720e8c9bda00b7688c76b03360a538bb1a",
    "us_1": "c705711154b1c514d7a0b5d133fabff42834110b198bd4cf86397d0d1c1597e9",
    "us_d": "6016cbdada120b2476e512e8c87c5d525f62ee8daa9f81e00c8caa1237477344"
}

def _getProjDir():
    return Path(os.path.realpath(__file__).split("tools")[0].rstrip(os.sep))
def getVerFile():
    return str(Path(_getProjDir()) / "data" / ".version")
def getDefaultVer():
    return 'eu'

def set_ver(version):
    with open(getVerFile(), 'w') as f:
        f.write(version)

def get_ver(version=None):
    if not os.path.exists(getVerFile()):
        set_ver(version or getDefaultVer())
        if not version: print (f"Note: Using default version \'{getDefaultVer()}\'")

    with open(getVerFile(), 'r') as f:
        ver = f.read()

    if len(ver) < 2:
        print ("Error: invalid version file")

    return ver
