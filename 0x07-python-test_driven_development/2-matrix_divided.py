#!/usr/bin/python3
"""Defines an divides all elements of a matrix function"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Args:
        matrix (_type_): _description_
        div (_type_): _description_
    """
    
    if type(div) not in [int, float]:
        raise TabError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    length_matrix = 0
    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if length_matrix != 0 and len(row) != length_matrix:
            raise TypeError("Each row of the matrix must have the same size")

        for num in row:
            if not type(num) in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        length_matrix = len(row)

    new_matrix = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return(new_matrix)
    
    