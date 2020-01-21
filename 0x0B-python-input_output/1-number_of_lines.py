#!/usr/bin/python3
""" Module point 1

    Description: Count the numbers of lines of a file
    Return: number lines"""


def number_of_lines(filename=""):
    """number_of_lines"""
    cont = 1
    with open(filename, 'r') as f:
        for line in f:
            if line.strip():
                cont += 1
    return cont
