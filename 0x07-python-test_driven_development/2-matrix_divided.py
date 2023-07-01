#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for e in row:
            if not isinstance(e, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round( e / div, 2))
        new_matrix.append(new_row)
    return new_matrix
