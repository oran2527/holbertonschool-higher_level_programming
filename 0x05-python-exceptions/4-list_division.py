#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        new = []
        res = 0.0
        flag = 0

        for x in range(0, list_length):
            res = my_list_1[x] / my_list_2[x]
            new.append(res)        
    except ZeroDivisionError:
        flag = 1
        res = 0
    except TypeError:
        flag = 2
        res = 0
    except IndexError:
        flag = 3
        res = 0
    finally:
        if flag == 1:
            print("division by 0")
        if flag == 2:
            print("wrong type")
        if flag == 3:
            print("out of range")
