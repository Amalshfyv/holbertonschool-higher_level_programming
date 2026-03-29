#!/usr/bin/python3

"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by
    a given divisor and rounds the result to 2 decimal places.

    Args:
        matrix (list of list of int/float): A matrix to be divided.
        div (int/float): The divisor (must be non-zero).

    Returns:
        list of list of float: A new matrix with
        each element divided and rounded to 2 decimal places.

    Raises:
        TypeError: If `div` is not a number,
        if `matrix` contains non-numeric elements,
        or if rows are not all the same length.
        ZeroDivisionError: If `div` is zero.
    """
    error = ("div must be a number",
             "division by zero",
             "Each row of the matrix must have the same size",
             "matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError(error[0])

    if div == 0:
        raise ZeroDivisionError(error[1])

    for row in matrix:
        if len(matrix) > 1 and len(row) != len(matrix[0]):
            raise TypeError(error[2])
        temp = []
        if isinstance(row, list):
            temp = row.copy()
        else:
            raise TypeError(error[3])
        for i in range(len(temp)):
            if not isinstance(temp[i], (int, float)):
                raise TypeError(error[3])
            temp[i] = round(temp[i] / div, 2)
        new_matrix.append(temp)
    return new_matrix
