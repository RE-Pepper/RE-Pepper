#!/usr/bin/env python3
import os
import re
import sys
import struct
from capstone import *
from capstone.arm import *
tools.low.glob import *
from splector._utils import *
tools.low.__updateMap import updateFull

# goal: find all function starts
# bl calls = sure
# datapool references = good
# data refs = okay
# mov r0,r0 unsure (no)

md = None

def main():
    print("To be made. Please focus on the EU version of the game, for now.")

if __name__ == "__main__":
    main()
