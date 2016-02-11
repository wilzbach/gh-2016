#!/usr/bin/env python
# encoding: utf-8

import sys
from parser import parse

if len(sys.argv) < 2:
    sys.exit("did you forget sth.?")

inFileName = sys.argv[1]
outFileName = sys.argv[2]


g = parse(inFileName)

print(g["warehouses"][0])

# do stuff
#


