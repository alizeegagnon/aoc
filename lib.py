#Author: FabriceCh

def read_file(path):
    arr = []
    with open(path, "r") as file:
        for line in file:
            arr.append(line.rstrip())
    return arr

#Author: Alizee

#### CARTESIAN LIB
#bogus function to be default in other functions
def bogus_bool_func(item):
    return True

# returns a list of adjacent coordinates (neighbors) 
# func is an additional boolean function on the array 
# diagonal is a boolean option
# array does not have to be square, but has to be rectangular
# array cannot be empty
def neighbors(i,j,arr, diag = True, func = bogus_bool_func):
    possibilities = [[i+1,j], [i,j+1],[i-1,j],[i,j-1]]
    if diag:
        possibilities += [[i-1,j-1],[i-1,j+1],[i+1,j-1],[i+1,j+1]]
    possibilities = [p for p in possibilities 
                     if p[0] >= 0 and p[1] >= 0 
                     and p[0] < len(arr) and p[1] < len(arr[0]) 
                     and func(arr[p[0]][p[1]])]

    return sorted(possibilities)

#this function takes in two coordinates and displays adjacency
#the coords can have a variable number of dimensions, but the same each
#it can be set to consider itself as adjacent (eq = True) or not
#it can be set to consider diagonals as adjacent (diag = True) or not
def adj(a,b,diag = True, selfeq = False):
    seen = False
    for i in range(len(a)):
        if not diag and abs(a[i]-b[i]) == 1:
            if seen:
                return False
            else:
                seen = True
        elif abs(a[i]-b[i]) > 1:
            return False
    return selfeq or a != b

#### BASIC UTILS

#print an array with one item per line
def aprint(arr):
    if len(arr) == 0:
        print("empty array")
    for i in range(len(arr)):
        print(str(i)+".",str(arr[i]))

#print a rectangular array of arrays and aligns the columns
#displays coordinates
def tprint(arr,separator=" "):
    lj = len(arr[0])
    ibuff = len(str(len(arr)))
    jbuff = len(str(lj))+1
    lj -= 1
    buffs = [0 for i in range(lj)]
    print("_"*(ibuff+2),end='')
    for j in range(lj):
        buffs[j] = max([len(str(a[j])) for a in arr]+[jbuff])
        print(str(j)+'_'+"_"*(buffs[j]-len(str(j))),end='')
    print(str(lj)+"_")
    for i in range(len(arr)):
        print(str(i)+". "+" "*(ibuff - len(str(i))),end='')
        for j in range(lj):
            w = str(arr[i][j])
            print(w + " "*(buffs[j]-len(w))+ separator,end='')
        print(str(arr[i][-1]))

##### INTERVALS LIB
#returns 0 if intersects, -1 if i1 is strictly below i2, and 1 if i1 is strictly above i2
#excl = True makes it so last integer of interval is not part of it
def compareIntervals(i1, i2, excl=True):
    if excl and ((i1[0] >= i2[0] and i1[0] < i2[1]) or (i1[1] > i2[0] and i1[1] <= i2[1]) or (i2[0] >= i1[0] and i2[0] < i1[1])):
        return 0
    elif not excl and ((i1[0] >= i2[0] and i1[0] <= i2[1]) or (i1[1] >= i2[0] and i1[1] <= i2[1]) or (i2[0] >= i1[0] and i2[0] <= i1[1])):
        return 0
    elif (excl and i1[1] <= i2[0]) or (not excl and i1[1] < i2[0]):
        return -1
    elif (excl and i1[0] >= i2[1]) or (not excl and i1[0] > i2[1]):
        return 1
    else:
        raise Exception("this is not supposed to happen")

#we return the whole interval i1, but partitioned by i2's interval
#the intervals cannot be empty or None
#the intervals are expected to intersect 
#otherwise the first return will return i1 and the others nothing
def leftJoin(i1,i2, excl=True):
    if compareIntervals(i1,i2,excl) != 0:
        return (i1, None, None)
    ma = max(i1[0],i2[0])
    mi = min(i1[1],i2[1])
    pre = [i1[0],ma]
    mid = [ma,mi]
    post = [mi,i1[1]]
    if not excl:
        pre[1] -= 1
    if post[0] == post[0]:
        post = None
    return (pre,mid,post)

def test_leftJoin():
    tests = []
    tests.append([[0,1],[1,2],False,([0,0],[1,1],None)]) # intersect on last one only, incl
    tests.append([[0,1],[1,2],True,([0,1],None,None)]) # no intersect since excl
    tests.append([[0,2],[1,2],True,([0,1],[1,2],None)]) # intersect on last one only, excl

    for t in tests:
        print(t[-1],leftJoin(*t[:-1]))
        assert t[-1] == leftJoin(*t[:-1])
    print("leftJoin unit tests passing")

test_leftJoin()
#if exclusive, delete equal intervals
def mergeIntervals(interval_list, excl = True):
    iList = sorted(interval_list)
    i = 0
    while i < len(iList):
        if iList[i][0] > iList[i][1] or (excl and iList[i][0] == iList[i][1]) :
            iList.pop(i)
        elif i > 0 and iList[i-1][1] >= iList[i][0]:
            iList[i-1] = [min(iList[i-1][0], iList[i][0]), max(iList[i-1][1], iList[i][1])]
            iList.pop(i)
        else:
            i+= 1
    return iList

##### UNIT TESTS

def test_compareIntervals():
    tests = []
    tests.append(([1,4],[1,5],0,0)) # l1 <= l2
    tests.append(([1,4], [4,5], -1,0)) # l1 < l2
    tests.append(((3,5), (1,4), 0,0)) # l1 >= l2
    tests.append(([4,7], [2,4], 1, 0)) # li > l2
    tests.append(([2,19],[4,6],0,0)) # l2 in l1
    tests.append(([4,6],[2,19],0,0)) # l1 in l2
    tests.append(([3,8],[-4,-5],1,1)) # l2 < l1
    tests.append(([-3,1],[4,15],-1,-1)) # l1 < l2

    for d in tests:
        assert compareIntervals(d[0], d[1], True) == d[2]
        assert compareIntervals(d[0], d[1], False) == d[3]
    print("compareIntervals unit tests passing")

def love(item):
    return item < 3

def test_neighbors():
    arr1 = [[1,2,3,4,5],[5,4,3,2,1],[1,2,3,2,1],[1,1,1,1,1],[2,4,2,5,2],[5,8,67,3,1]]
    arr2 = [[0]]
    arr3 = [[2,3,4]]
    tests = []
    tests.append([0,0,arr1,True,[[0,1],[1,0],[1,1]]]) #    nwcornerd
    tests.append([5,0,arr1,True,[[5,1],[4,0],[4,1]]]) #    swcornerd
    tests.append([5,4,arr1,True,[[5,3],[4,4],[4,3]]]) #    secornerd
    tests.append([0,4,arr1,True,[[0,3],[1,4],[1,3]]]) #    necornerd
    tests.append([0,0,arr1,False,[[0,1],[1,0]]]) #    nwcorner
    tests.append([5,0,arr1,False,[[5,1],[4,0]]]) #    swcorner
    tests.append([5,4,arr1,False,[[5,3],[4,4]]]) #    secorner
    tests.append([0,4,arr1,False,[[0,3],[1,4]]]) #    necorner
    tests.append([0,0,arr2,True,[]]) #    nothingd
    tests.append([0,0,arr2,False,[]]) #    nothing
    tests.append([0,0,arr3,True,[[0,1]]]) #    lineleftd
    tests.append([0,1,arr3,True,[[0,0],[0,2]]]) #    linemidd 
    tests.append([0,2,arr3,True,[[0,1]]]) #    linerightd
    tests.append([0,0,arr3,False,[[0,1]]]) #    lineleft
    tests.append([0,1,arr3,False,[[0,0],[0,2]]]) #    linemid 
    tests.append([0,2,arr3,False,[[0,1]]]) #    lineright
    tests.append([0,0,arr1,True,love,[[0,1]]]) #    nwcornerdl
    tests.append([5,0,arr1,True,love,[[4,0]]]) #    swcornerdl
    tests.append([5,4,arr1,True,love,[[4,4]]]) #    secornerdl
    tests.append([0,4,arr1,True,love,[[1,4],[1,3]]]) #    necornerdl
    tests.append([0,0,arr1,False,love,[[0,1]]]) #    nwcornerl
    tests.append([5,0,arr1,False,love,[[4,0]]]) #    swcornerl
    tests.append([5,4,arr1,False,love,[[4,4]]]) #    secornerl
    tests.append([0,4,arr1,False,love,[[1,4]]]) #    necornerl
    tests.append([0,0,arr2,True,love,[]]) #    nothingdl
    tests.append([0,0,arr2,False,love,[]]) #    nothingl
    tests.append([0,0,arr3,True,love,[]]) #    lineleftdl
    tests.append([0,1,arr3,True,love,[[0,0]]]) #    linemiddl 
    tests.append([0,2,arr3,True,love,[]]) #    linerightdl
    tests.append([0,0,arr3,False,love,[]]) #    lineleftl
    tests.append([0,1,arr3,False,love,[[0,0]]]) #    linemidl 
    tests.append([0,2,arr3,False,love,[]]) #    linerightl
    tests.append([2,2,arr1,False,[[1,2],[2,3],[2,1],[3,2]]]) # middle
    tests.append([2,2,arr1,True,[[1,2],[2,3],[2,1],[3,2],[1,3],[3,1],[1,1],[3,3]]]) # middled
    tests.append([2,2,arr1,False,love,[[2,3],[2,1],[3,2]]]) # middlel
    tests.append([2,2,arr1,True,love,[[2,3],[2,1],[3,2],[1,3],[3,1],[3,3]]]) # middledl

    for t in tests:
        assert neighbors(*t[:-1]) == sorted(t[-1])
    print("neighbors unit tests passing")

def test_adj():
    tests = []
    tests.append([[],[],True,True,True]) # 0d
    tests.append([[],[],True,False,False]) # 0d s
    tests.append([[],[],False,True,True]) # 0d d
    tests.append([[],[],False,False,False]) # 0d s d
    tests.append([[0],[1],True,True,True]) # 1d up
    tests.append([[0],[2],True,True,False]) # 1d too up
    tests.append([[0],[-1],True,True,True]) # 1d down
    tests.append([[0],[-12312],True,True,False]) # 1d too down 
    tests.append([[0],[0],True,True,True]) # 1d equal 
    tests.append([[0],[0],True,False,False]) # 1d s equal 
    tests.append([[0],[1],False,True,True]) # 1d d up
    tests.append([[0],[1],True,False,True]) # 1d s up
    tests.append([[0],[1],False,False,True]) # 1d s d up
    tests.append([[0],[-1],False,True,True]) # 1d d down
    tests.append([[0],[-1],True,False,True]) # 1d s down
    tests.append([[0],[-1],False,False,True]) # 1d s d down
    tests.append([[0,0],[1,1],True,True,True]) # 2d nw 
    tests.append([[0,0],[0,1],True,True,True]) # 2d n
    tests.append([[0,0],[-1,1],True,True,True]) # 2d ne
    tests.append([[0,0],[-1,0],True,True,True]) # 2d e
    tests.append([[0,0],[-1,-1],True,True,True]) # 2d se 
    tests.append([[0,0],[0,-1],True,True,True]) # 2d s
    tests.append([[0,0],[1,-1],True,True,True]) # 2d sw
    tests.append([[0,0],[1,0],True,True,True]) # 2d w
    tests.append([[0,0],[1,1],False,True,False]) # 2d nw d 
    tests.append([[0,0],[0,1],False,True,True]) # 2d n d
    tests.append([[0,0],[-1,1],False,True,False]) # 2d ne d
    tests.append([[0,0],[-1,0],False,True,True]) # 2d e d
    tests.append([[0,0],[-1,-1],False,True,False]) # 2d se  d
    tests.append([[0,0],[0,-1],False,True,True]) # 2d s d
    tests.append([[0,0],[1,-1],False,True,False]) # 2d sw d
    tests.append([[0,0],[1,0],False,True,True]) # 2d w d
    tests.append([[0,0],[0,0],True,True,True]) # 2d equal
    tests.append([[0,0],[0,0],True,False,False]) # 2d s equal
    tests.append([[0,0],[0,0],False,True,True]) # 2d d equal
    tests.append([[0,0],[0,0],False,False,False]) # 2d s d equal
    tests.append([[0,0],[2,2],True,True,False]) # 2d nw far 
    tests.append([[0,0],[2,1],True,True,False]) # 2d nw far 
    tests.append([[0,0],[1,2],True,True,False]) # 2d nw far 
    tests.append([[0,0],[0,2],True,True,False]) # 2d n far
    tests.append([[0,0],[-2,2],True,True,False]) # 2d ne far
    tests.append([[0,0],[-2,1],True,True,False]) # 2d ne far
    tests.append([[0,0],[-1,2],True,True,False]) # 2d ne far
    tests.append([[0,0],[-2,0],True,True,False]) # 2d e far
    tests.append([[0,0],[-2,-2],True,True,False]) # 2d se far
    tests.append([[0,0],[-2,-1],True,True,False]) # 2d se far
    tests.append([[0,0],[-1,-2],True,True,False]) # 2d se far
    tests.append([[0,0],[0,-2],True,True,False]) # 2d s far
    tests.append([[0,0],[2,-2],True,True,False]) # 2d sw far
    tests.append([[0,0],[2,-1],True,True,False]) # 2d sw far
    tests.append([[0,0],[1,-2],True,True,False]) # 2d sw far
    tests.append([[0,0],[2,0],True,True,False]) # 2d w far
    tests.append([[0,0,0,0],[0,0,1,1],True,True,True]) #4d diag
    tests.append([[0,0,0,0],[0,0,1,1],False,True,False]) #4d d diag
    tests.append([[0,0,0,0],[0,0,0,0],True,False,False]) #4d s equal
    tests.append([[0,0,0,0],[0,0,0,0],True,True,True]) #4d equal
    tests.append([[0,0,0,0],[1,0,0,0],False,True,True]) #4d d 1
    tests.append([[0,0,0,0],[0,1,0,0],False,True,True]) #4d d 2
    tests.append([[0,0,0,0],[0,0,1,0],False,True,True]) #4d d 3
    tests.append([[0,0,0,0],[0,0,0,1],False,True,True]) #4d d 4
    
    for t in tests:
        assert t[-1] == adj(*t[:-1]) 
    print("adj unit tests passing")
def test_tprint():
    a = [[1,3,5,32423,"dfsd",0,0,0,0,0,0],["allo","",12310,1,1,1,1,1,1,1,1],["allo","",12310,1,1,1,1,1,1,1,1],["allo","",12310,1,1,1,1,1,1,1,1],["allo","",12310,1,1,1,1,1,1,1,1],["allo","",12310,1,1,1,1,1,1,1,1],["allo","",12310,1,1,1,1,1,1,1,1],["allo","",12310,1,1,1,1,1,1,1,1],["allo","",12310,1,1,1,1,1,1,1,1],["allo","",12310,1,1,1,1,1,1,1,1],["allo","",12310,1,1,1,1,1,1,1,1],["allo","",12310,1,1,1,1,1,1,1,1]]
    tprint(a)
    print("if the above is aligned, then tprint is probably fine")

def run_unit_tests():
    test_compareIntervals()
    test_neighbors()
    test_adj()
    test_tprint()
    print("unit tests all passing")

run_unit_tests()
