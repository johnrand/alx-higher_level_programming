#!/usr/bin/python3

"""
This module creates a class reactangle that inherits from the base class.

"""

from models.base import Base


class Rectangle(Base):
    """
    The class rectangle inherits from the base class.

    Attributes:
        width: The width of the rectangle.
        height: The height of the rectangle.
        x: x-coordinate of the rectangle's position.
        y: y-coordinate of the rectangle's position.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x: x-coordinate of the rectangle's position.
            y: y-coordinate of the rectangle's position.
            id: The identifier for the object.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """
            Getter method for the width attribute.
            """
            return self.__width

        @width.setter
        def width(self, value):
            """
            Setter method for the width attribute.

            Args:
                value: value to set for the width.
            """
            self.__width = value

        @property
        def height(self):
            """
            Getter method for the height attribute.
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            Setter method for the height attribute.

            Args:
                value: value to set for the height.
            """
            self.__height = value

        @property
        def x(self):
            """
            Getter method for the x attribute.
            """
            return self.__x

        @x.setter
        def x(self, value):
            """
            Setter method for the x attribute.

            Args:
                value: value to set for the x-coordinate.
            """
            self.__x = value

        @property
        def y(self):
            """
            Getter method for the y attribute.
            """
            return self.__y

        @y.setter
        def y(self, value):
            """
            Setter method for the y attribute.

            Args:
                value: value to set for the y-coordinate.
            """
            self.__y = value
