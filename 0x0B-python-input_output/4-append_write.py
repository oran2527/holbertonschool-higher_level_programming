#!/usr/bin/python3
""" Module point 4

    Description: Append string at the end of a file
    Return: Number of characters added"""


def append_write(filename="", text=""):
    """append_write"""

    with open(filename, 'a+') as f:
        n_c = f.write(text)
    return n_c
