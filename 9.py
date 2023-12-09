import sys
import functools
from lib import (
    read_file
    )

if len(sys.argv) > 1:
    test_run = int(sys.argv[1])
else:
    test_run = 1


if test_run == 1:
    arr = read_file("exem")
else:
    arr = read_file("input")
part1 = False
sum = 0
if part1:
    for line in arr:
        line = [int(i) for i in line.split(" ")]
        iter = len(line)
        while iter > 0 and line[:iter] != [0 for i in range(iter)]:
            iter -= 1
            for i in range(iter):
                line[i] = line[i+1]-line[i]
        for i in range(len(line)-1):
            if line[i] != 0:
                line[i+1] += line[i]
        sum += line[-1]
else:
    for line in arr:
        line = [int(i) for i in line.split(" ")]
        iter = 0
        while iter < len(line) and line[iter:] != [0 for i in range(len(line)-iter)]:
            for i in range(len(line)-1,iter,-1):
                line[i] = -(line[i-1]-line[i])
            iter += 1

        for i in range(len(line)-1,-1,-1):
            if line[i] != 0:
                line[i-1] -= line[i]
        sum += line[0]

print(sum)
