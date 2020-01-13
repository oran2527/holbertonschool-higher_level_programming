#!/usr/bin/python3
"""matrix_divided - div of list of list by an element

   Description: return a list of list with the division by element
   Return: list of list
"""


def matrix_divided(matrix, div):
    """matrix_divided - function.
       matrix - first value.
       div - second value."""
    new = []
    new.append([])
    new.append([])

    if div is 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    for i in range(0, len(matrix)):
        try:
            len(matrix[i])
        except:
           raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
        for j in range(0, len(matrix[i])): 
            if i > 0 and len(matrix[i]) != len(matrix[i - 1]):
                raise TypeError("Each row of the matrix\
 must have the same size")
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            new[i].append(round(matrix[i][j] / div, 2))
    return new
