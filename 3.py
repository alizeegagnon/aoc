from lib import (
    read_file,
    lookAround,
    isDiagonalAdj
    )

test_run = 1
if test_run == 0:
    a = read_file("exem")
else:
    a = read_file("input")

symbols = {"*", "#", "$", "&", "%", "^", "!", "@", "+", "=", "/", "-"}
arr = []
for line in a:
    arr.append([*line])

nu = {"1","2","3","4","5","6","7","8","9","0"}

def isNum(item):
    return item in nu

def getNum(i,j,arr):
    if arr[i][j] not in nu:
        return 0 , arr

    n = arr[i][j]
    j1 = j + 1
    while j1 < len(arr) and arr[i][j1] in nu:
        n += arr[i][j1]
        arr[i][j1] = "."
        j1 += 1
    j1 = j-1
    while j1 >= 0 and arr[i][j1] in nu:
        n = arr[i][j1] + n
        arr[i][j1] = "."
        j1 -= 1
    return int(n), arr

su = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] in symbols:
            if arr[i][j] != "*":
                continue
            print(lookAround(i,j,arr, isNum))
            mul = 1
            seen = 0
            for k,l in lookAround(i,j,arr, isNum):
                n, arr = getNum(k,l,arr)
                if n > 0:
                    seen += 1
                    mul *= n
                    if seen == 2:
                        su += mul
                        break

print(su)
                
