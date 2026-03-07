#!/usr/bin/env python3
from tools.pypstem._utils import *
from tools.pypstem.callProcess import do_link
from tools.low.glob import *
from tools.low.__genScatter import gen_scatter
# todo: compile_commands.json
# todo: scatter map
# todo: map file
# todo: that one other funny file maybe
# note: force these (link): --cpu=MPCore --fpu=VFPv2 --startup=__ctr_start --entry=__ctr_start --keep=nnMain --datacompressor=off --verbose --mangled --map

def exec_link():
    echo ("Generating scatter")
    gen_scatter()

    
