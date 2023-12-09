import sys
import functools
from lib import (
    read_file,
    aprint,
    compareIntervals,
    leftJoin,
    mergeIntervals
    )

if len(sys.argv) > 1:
    test_run = int(sys.argv[1])
else:
    test_run = 1


if test_run == 1:
    arr = read_file("exem")
else:
    arr = read_file("input")

str = {'A':13, 'K':12, 'Q':11, 'J':-1, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':0}

def isStr(a,b):
    if str[a] > str[b]:
        return 1
    elif  str[a] == str[b]:
        return 0
    else:
        return -1

def ctype(hand):
    h = sorted(hand)
    
    d = {}
    seen = False
    for h1 in h:
        if h1 in d:
            d[h1] += 1
        else:
            d[h1] = 1
        if h1 == 'J':
            seen = True
    j = 0
    if seen:
        j = d['J']
        del(d['J'])
    if j == 5:
        return 7
    m = sorted(d.values())
    m[-1] += j
    if m == [5]:
        return 7
    elif m == [1,4]:
        return 6
    elif m == [2,3]:
        return 5
    elif m == [1,1,3]:
        return 4
    elif m == [1,2,2]:
        return 3
    elif m == [1,1,1,2]:
        return 2
    elif  m == [1,1,1,1,1]:
        return 1
    
sum = 0
arr = [line.split(" ") for line in arr]
#arr = [[ctype(line[0])]+line for line in arr]
def isbigger(hand1,hand2):
    h1 = hand1[0]
    h2 = hand2[0]
    if ctype(h1) > ctype(h2):
        return 1
    elif ctype(h1) < ctype(h2):
        return -1
    else:
        for i in range(len(h1)):
            if isStr(h1[i],h2[i]) == 1:
                return 1
            elif isStr(h2[i],h1[i]) == 1:
                return -1
    return 0
arr.sort(key=functools.cmp_to_key(isbigger))
for i in range(len(arr)):
    print(arr[i][0])
    sum += int(arr[i][1]) * (i+1)
print(sum)
