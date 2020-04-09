#!/usr/bin/python3
''' point 6 find a peak in a list '''


def find_peak(list_of_integers):
    ''' function to find the max value in a list '''
    if list_of_integers != []:
        end = len(list_of_integers)
        list_of_integers.sort(reverse=False)
        return list_of_integers[end - 1]
    else:
        return None
