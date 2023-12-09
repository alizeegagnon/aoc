import sys
from lib import (
    read_file,
    aprint,
    compareIntervals,
    leftJoin,
    mergeIntervals
    )

if len(sys.argv) > 1:
    test_run = sys.argv[1]
else:
    test_run = 0

if test_run == 1:
    arr = read_file("exem")
else:
    arr = read_file("input")

def seedRanges(seedLine):
    seedLine = [int(i) for i in seedLine]
    seedranges = []
    for i in range(len(seedLine)):
        if i % 2 == 1:
            seedLine[i] += seedLine[i-1]
            seedranges.append(seedLine[i-1:i+1])
    return sorted(seedranges)

def mapToRangeAndDiff(weird_map):
    source = weird_map[1]
    dest = weird_map[0]
    range_len = weird_map[2]
    diff = dest - source
    map_range_diff = ([source, source + range_len], diff)
    return map_range_diff

#loop through two lists at once
def rotate(seeds, rrange):
    s = 0
    r = 0
    extra_seeds = []
    while s < len(seeds) and r < len(rrange):
        seed = seeds[s]
        ra = rrange[r]
        comp = compareIntervals(seed,ra[0])
        if comp == -1:
            s += 1
        elif comp == 0:
            pre_seed, permut, seed = leftJoin(seed,ra[0])
            extra_seeds.append(pre_seed)
            extra_seeds.append([i + ra[1] for i in permut])
            stra = extra_seeds[-1]
            seeds[s] = seed
            if seed[0] == seed[1]:
                s += 1
            else:
                r += 1
        elif comp == 1:
            r += 1
    seeds += extra_seeds
    return mergeIntervals(seeds)

#to debug, or to follow the outcome of a single seed like in part 1
def mapOneNumber(seed, mappings, start=0, stop = 0):
    if stop == 0:
        stop = len(mappings)
    for i in range(start,stop):
        for mapping in mappings[i]:
            if seed >= mapping[0][0] and seed < mapping[0][1]:
                seed += mapping[1]
                break
    return seed

seeds = []
mappings = []
#actually the first category:
last_category = "seed"
#parsing stuff
for line in arr:
    line = line.split(" ")
    if len(line) < 2:
        continue
    elif line[0] == "seeds:":
        #part 1 input:
        #seeds = sorted([[int(i),int(i)+1] for i in line[1:]])
        #part 2 input:
        seeds = seedRanges(line[1:])
    elif line[1] == "map:" and line[0].split("-")[0] == last_category:
        last_category = line[0].split("-")[2]
        mappings.append([])
    else:
        line = [int(i) for i in line]
        mappings[-1].append(mapToRangeAndDiff(line)) 

#Have they tried to trick us ??
assert last_category == "location"
#compute stuff
for mapping in mappings:
    mapping.sort()
    seeds = rotate(seeds, mapping)

#print the answer
print(seeds[0][0])
