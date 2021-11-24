#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for c in matrix:
        result = list(map(lambda x: x**2, c))
        new_matrix.append(result)
    return new_matrix
