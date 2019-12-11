#!/usr/bin/python3
def print_last_digit(number):
    l = 0
    l = abs(number) % 10
    print("{:d}".format(l), end="")
    return l
