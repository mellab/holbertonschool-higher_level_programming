#!/usr/bin/python3

"""
This module contains the following instructions:
- def matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    message_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(message_type)

    length = 0
    message_size = "Each row of the matrix must have the same size"

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(message_type)

        if length != 0 and len(elements) != length:
            raise TypeError(message_size)

        for num in elements:
            if not type(num) in (int, float):
                raise TypeError(message_type)

        length = len(elements)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
