#!/usr/bin/python3
"""
module point 1
"""


def number_of_lines(filename=""):
    """Return the number of lines"""
    cont = 0
    with open(filename, 'r') as f:
        for line in f:
            cont = cont + 1
    return cont
