#!/usr/bin/python3
def pow(a, b):
    pot = 1
    c = b
    if b != 0:
        for x in range(1, abs(b) + 1):
            pot *= a
    else:
        pot = 1
    if c < 0:
        pot = 1 / pot
    return pot
