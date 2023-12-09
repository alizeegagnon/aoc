from parse import read_file

a = read_file("input")
numbers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9","1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9"}
rumbers = {"eno":"1", "owt":"2", "eerht":"3", "ruof":"4", "evif":"5", "xis":"6", "neves":"7", "thgie":"8", "enin":"9","1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9"}

def geee(line):
    mi = ""
    m = len(line)
    for n in list(numbers.keys()):
        try:
            a = line.index(n)
        except ValueError:
            a = len(line)
        if a < m:
            mi = numbers[n]
            m = a
    return mi

def reee(line):
    mi = ""
    m = len(line)
    for n in list(rumbers.keys()):
        try:
            a = line.index(n)
        except ValueError:
            a = len(line)
        if a < m:
            mi = rumbers[n]
            m = a
    return mi

s = 0
for line in a:
    n = ""
    n += geee(line)
    n += reee(line[::-1]) 
    s += int(n)
print(s)



