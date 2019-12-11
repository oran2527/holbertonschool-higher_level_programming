#!/usr/bin/python3
for n in range(0, 10):
    for x in range(0, 10):
        if x != 0 or n != 0:
            print(", ", end="")
        print("{:d}{:d}".format(n, x), end="")
