#!/usr/bin/env python
# encoding: utf-8

import sys
from parser import parse
from serializer import serialize

if len(sys.argv) < 2:
    sys.exit("did you forget sth.?")

inFileName = sys.argv[1]
outFileName = sys.argv[2]


g = parse(inFileName)

print(g["warehouses"][0])
print(g["orders"][0])
commands = []
commands.append([0, "L", 0, 0, 1])
serialize(outFileName, commands)
