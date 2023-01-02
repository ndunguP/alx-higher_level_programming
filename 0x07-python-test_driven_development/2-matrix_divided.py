#!/usr/bin/python3
"""Divide matrix elements module"""


def matrix_divided(matrix, div):
    """matrix_divided - divied a matrix
    
        Args:
            matrix - list of lists
            div - number matrix elements are to be divided by
        Returns:
            new matrix with divided elements
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or matrix is None:
        raise TypeError(error)
    new_list = []
    if type(div) is not int and type(div) is not float or div is None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if len(matrix[0]) != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        if type(i) is not list:
            raise TypeError(error)
        for j in i:
            if (type(j) is not int and type(j) is not float):
                raise TypeError(error)
    new_list = [[round(x / div, 2) for x in row]for row in matrix]
    return new_list
