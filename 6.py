from lib import read_file

test_run = 0
if test_run == 1:
    arr = read_file("eexem")
else:
    arr = read_file("iinput")

times = arr[0].split(" ")[1:]
times = [int(t) for t in times]
dists = arr[1].split(" ")[1:]
dists = [int(t) for t in dists]

small = 0
for t in range(1,times[0]-1):
    if t*(times[0]-t) > dists[0]:
        small = t -1
        break
print(times[0]-small-small)
