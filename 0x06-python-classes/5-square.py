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
        """
        Initializing this square class

        Args:
            size: size of the square defined

        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
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
        Value: value returned
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Takes no arguments
        Return the area of the square

        """
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")

        return (self.__size ** 2)

    def my_print(self):
        """
        Prints the square with the character # to stdout
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
