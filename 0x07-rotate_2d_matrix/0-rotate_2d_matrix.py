#!/usr/bin/python3
"""
A rotate_2d_matrix module
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in place.

    Parameters:
    Matrix (list of list of int): The n x n 2D matrix
    to be rotated.

    Returns:
    None: The function modifies the input matrix in place.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
