from parse import read_file

test_run = 1
if test_run == 1:
    a = read_file("exem")
else:
    a = read_file("input")

#part 1
m = {"green":13, "red":12, "blue":14}

def check(draw):
    draw = draw.split(",")
    for g in draw:
        qty = g.split(" ")
        if m[qty[1]] < int(qty[0]):
            return False
    return True

s = 0
for line in a:
    ok = True
    line = line.split(":")
    game = line[0]
    line = line[1].split(";")
    for draw in line:
        if not check(draw):
            ok = False
            break
    if ok:
        s+= int(game)
print(s)

#part 2
s = 0


def mult(line):
    q = {"green":0, "red":0, "blue":0}
    for draw in line:
        draw = draw.split(",")
        for w in draw:
            w = w.split(" ")
            if int(w[0]) > q[w[1]]:
                q[w[1]] = int(w[0])
    return q["green"]*q["red"]*q["blue"]

for line in a:
    ok = True
    line = line.split(":")
    game = line[0]
    line = line[1].split(";")
    s += mult(line)

print(s)



