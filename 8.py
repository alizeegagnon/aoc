import sys
import functools
from lib import (
    read_file,
    aprint
    )

if len(sys.argv) > 1:
    test_run = int(sys.argv[1])
else:
    test_run = 1


if test_run == 1:
    arr = read_file("exem")
else:
    arr = read_file("input")

dirs = arr[0]
dirs = dirs.replace('R','1')
dirs = dirs.replace('L','0')
ass = []
azz = []
nodes = {}
for line in arr[2:]:
    line = line.split(" = ")
    ou = line[1][1:-1].split(", ")
    nodes[line[0]] = ou
    if line[0][2] == 'A':
        ass.append(line[0])
    elif line[0][2] == 'Z':
        azz.append(line[0])

def isAllZ(nods):
    for n in nods:
        if n[2] != 'Z':
            return False
    return True

asz = [0,0,0,0,0,0]
inst = 0
count = 0
start = [27878, 35242, 38398, 31034, 24722, 41554]
mods = [13939, 17621, 19199, 15517, 12361, 20777]

def isAllEqual(l):
    return l[1:] == l[:-1]

i = 0
maxs = 41554
count = 0
while not isAllEqual(start):
    while start[i] < maxs:
        start[i] += mods[i]
    maxs = start[i]
    i += 1
    i %= 6
    count += 1
    if count % 33554432 == 0:
        print(count,maxs,start)

print(start)

