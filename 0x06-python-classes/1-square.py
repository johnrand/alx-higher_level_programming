#!/usr/bin/python3

"""
This module defines a square class with a private instance

"""


class Square:
    """
    It defines a square with a private instance attribute 'size'.

    """

    def __init__(self, size=None):
        """The constructor for the Square class.

        Args:
            size: The size of the square.

        Note:
            The size is a private attribute.
        """
        self.__size = size
