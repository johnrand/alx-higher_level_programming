#!/usr/bin/python3

"""
This module validate the size attribute and raises error if
not an integeri and returns the square

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

    def area(self):
        """
        Takes no arguments
        Return the area of the square

        """
        return self.size * self.size
