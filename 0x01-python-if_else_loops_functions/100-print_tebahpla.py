#!/usr/bin/python3
for l in range(122, 96, -1):
    rest = 0
    if l % 2 != 0:
        rest = 32
    print("{:c}".format(l - rest), end="")
