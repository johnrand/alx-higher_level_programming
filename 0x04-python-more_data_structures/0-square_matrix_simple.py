#!/usr/bin/python3

"""
    square_matrix_simple.py:
        function that computes the square value of all integers of a matrix
        and returns new matrix same size as original.
        Each value is the square of the value of input
    matrix:
        the matrix
"""


def square_matrix_simple(matrix=[]):
    new_matrix = [[integer**2 for integer in row] for row in matrix]
    return new_matrix
