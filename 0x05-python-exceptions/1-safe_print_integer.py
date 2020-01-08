#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if int(value) - int(value) is 0:
            print("{:d}".format(int(value)))
            return True
    except ValueError:
        return False
