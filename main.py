#!/usr/bin/env python
# encoding: utf-8

import sys
from parser import parse
from serializer import serialize
from schedule import schedule

if len(sys.argv) < 2:
    sys.exit("did you forget sth.?")

inFileName = sys.argv[1]
outFileName = sys.argv[2]

state = parse(inFileName)
commands = schedule(state)
serialize(outFileName, commands)
