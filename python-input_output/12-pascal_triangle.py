#!/usr/bin/python3
"""This module contains pascal_triangle() function"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(1, i):
            temp.append(triangle[i-1][j-1] + triangle[i-1][j])
        temp.append(1)
        triangle.append(temp)
    return triangle
