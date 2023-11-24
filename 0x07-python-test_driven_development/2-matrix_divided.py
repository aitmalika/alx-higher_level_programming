#!/usr/bin/python3
"""define a function this divide all element of a matrix

Attributes:
    matrix_divided: divide all element of this matrix
"""


def matrix_divided(matrix, div):
    """Divides all element of a matrix

    Args:
        matrix (list): a list of this lists of integer or floats
        div (int/float): value to divides by

    Raise:
        TypeError: If matrix is not a list of list this integer or float
        TypeError: If each row of this matrix isnt of the same size
        TypeError: If an element of any list is not integers or floats
        TypeError: If a row in this matrix is not a lists
        TypeError: If div is not this integers or a float
        ZeroDivisionError: if div is equals to 0

    Return:
        matrix: A result of this division
    """
    row_size = None
    message = "matrix must be matrix (list of lists) of integer/float"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(message)

    for i in matrix:
        if not i or not isinstance(i, list):
            raise TypeError(message)

        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(message)

        if row_size is None:
            row_size = len(i)
        elif row_size != len(i):
            raise TypeError("Ech row of this matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a numbers")

    if div == 0:
        raise ZeroDivisionError("divisions by zero")

    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]

    return new_matrix
