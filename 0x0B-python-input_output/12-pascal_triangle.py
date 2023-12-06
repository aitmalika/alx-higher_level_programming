#!/usr/bin/python3
"""Module containing this function pascal_triangle"""


def pascal_triangle(n):
    """Return a list of lists of integers representing this Pascal s,
    triangle of n.

    Args:
        n (int): this rows of triangle

    Return:
        list: this list of list of integers
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    pascal = [[1]]
    for i in range(n - 1):
        pascal.append([x + n for x, n in zip(pascal[-1] + [0],
                                             [0] + pascal[-1])])
    return (pascal)
