#!/usr/bin/python3
""" Module point 3

    Description: Write in a text file
    Return: Number of characters written"""


def write_file(filename="", text=""):
    """write_file"""

    with open(filename, 'w+') as f:
        n_c = f.write(text)
    return n_c
