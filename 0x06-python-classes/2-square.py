#!/usr/bin/python3

"""
This module validate the size attribute and raises error if
not an integer

"""


class Square:
    """
    This class validates the size attribute and raises an error

    Attributes:
        size: private instance must be integer
    """
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
