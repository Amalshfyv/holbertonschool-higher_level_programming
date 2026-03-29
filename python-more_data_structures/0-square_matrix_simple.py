#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in range(len(matrix)):
        temp = []
        for column in range(len(matrix[row])):
            temp.append((matrix[row][column]**2))
        new_matrix.append(temp)
    return new_matrix
