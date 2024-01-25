#!/usr/bin/python3

class Square:
    """This is the Square class.

    It defines a square with a private instance attribute 'size'.
    """

    def __init__(self, size=0):
        """The constructor for the Square class.

        Args:
            size (int): The size of the square.

        Note:
            The size is a private attribute.
        """
        self.__size = size

    @property
    def dict_(self):
        """Getter method for obtaining a dictionaty representation of
        the square class.

        Returns:
            dict: A dictionary containing the size of the square.
        """
        return ('size': self.__size)


# Print documentation for the module
print(__doc__)

# Print documentation for the Square class
print(Square.__doc__)
