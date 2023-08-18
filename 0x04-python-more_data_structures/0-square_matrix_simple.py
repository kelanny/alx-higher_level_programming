#!/usr/bin/python3
# 0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    temp_matrix = matrix.copy()
    for i in range(len(temp_matrix)):
        temp_matrix[i] = list(map(lambda x: x**2, matrix[i]))
    return(temp_matrix)
