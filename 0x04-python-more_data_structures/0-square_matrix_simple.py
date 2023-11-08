#!/usr/bin/python3
def square_matrix_simple(matrix=[]):   
    new_matrix = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            new_matrix[row][col] = matrix[row][col] ** 2
    return new_matrix
