from lib import read_file

test_run = 0
if test_run == 1:
    arr = read_file("exem")
else:
    arr = read_file("input")




s = 0
sc = [1 for i in range(len(arr))]
for i in range(len(arr)):
    print(arr[i])
    line = arr[i].split(':')
    line = line[1].split('|')
    win = line[0].split(' ')
    win = [int(n) for n in win]
    numb = line[1].split(' ')
    numb = [int(n) for n in numb]
    a = 0
    for n in numb:
        if n in win:
           a+=1

    s += sc[i]
    for j in range(i+1,i+a+1):
        sc[j] += sc[i]

print(s)


