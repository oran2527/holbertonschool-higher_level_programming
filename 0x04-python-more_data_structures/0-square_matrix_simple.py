#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [] * 3
    matrix2 = [new] * len(new)
    for i in range(0, len(matrix)):
        new = []
        for j in range(0, len(matrix[i])):
            a = matrix[i][j] ** 2
            new.append(a)
        matrix2.append(new)
    return matrix2
