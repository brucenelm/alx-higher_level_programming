#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for i in r:
            if i != r[-1]:
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end="")
        print()

