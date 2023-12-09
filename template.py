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

for line in arr:
    print(line)
