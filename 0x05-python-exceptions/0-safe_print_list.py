#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    import sys
    try:
        for x in range(0, x):
            print(my_list[x], end="")
        print("\n", end="")    
        return x + 1
    except IndexError:
        i = 0
        print("\n", end="")
        for x in my_list:
            i = i + 1
        return i
