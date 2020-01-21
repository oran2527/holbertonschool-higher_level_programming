#!/usr/bin/python3
""" Module point 2

    Description: Print n lines
    Return: content of the n lines"""


def read_lines(filename="", nb_lines=0):
    """read_lines"""
    cont = 1
    with open(filename, 'r') as f:
        for line in f:
            if line.strip():
                cont += 1
    if nb_lines <= 0 or nb_lines >= cont:
        with open(filename, 'r') as r:
            print(r.read(), end="")
    else:
        cont = 1
        with open(filename, 'r') as d:
            for line in d:
                if cont < nb_lines + 1:
                    print(line, end="")
                    cont += 1
