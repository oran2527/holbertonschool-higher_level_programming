#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    import sys
    cont = 0

    try:
        for x in range(0, x):
            if type(my_list[x]) == int:
                print(my_list[x], end="")
                cont = cont + 1
        print("\n", end="")
        return cont
    except IndexError:
        raise IndexError
