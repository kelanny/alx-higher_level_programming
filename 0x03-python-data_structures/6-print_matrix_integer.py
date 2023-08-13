#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for lst in matrix[:]:
        for i in lst[:]:
            print("{:d}".format(i), end=" ")
        print()
