#!/usr/bin/python3
"""Defines a function that multiplies deux matrix by using the module NumPy.

Attributes:
    m_a (matrix)
    m_b (matrix)
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrix using numpy

    Args:
        m_a (matrice): first matrice
        m_b (matrice): second matrix

    Return:
        matrice: the product of this two matrice
    """
    # m_a = ([1, 2], [3, 4])
    # m_b = [[1, 2], [3, 4]]
    return np.matmul(m_a, m_b)
