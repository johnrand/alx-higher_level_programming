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

        @property
        def size(self):
            """
            Getter to return the size

            """
            return self.__size

        @size.setter
        def size(self, value):
            """
            Setter to return the value
            Vallu: value returned

            """
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    def area(self):
        """
        Takes no arguments
        Return the area of the square

        """
        return self.__size ** 2
