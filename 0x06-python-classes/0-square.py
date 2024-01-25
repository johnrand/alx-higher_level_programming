#!/usr/bin/python3

class Square:
    """This is the Square class.

    It represents a square and is currently empty, serving as a placeholder.
    """

    def __init__(self):
        """The constructor for the Square class.

        Currently, it initializes an empty square object.
        """
        pass

    def square_fnctn(self):
        """Example method inside the Square class.

        This method does nothing.
        """


def square_fnctn():
    """Example function outside the Square class.

    This function does nothing.
    """


# Print documentation for the module
print(__doc__)

# Print documentation for the Square class
print(Square.__doc__)

# Print documentation outside the class
print(square_fnctn.__doc__)

# Print documentation inside the Square class
print(Square.square_fnctn.__doc__)
