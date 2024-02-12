#!/usr/bin/python3

"""
A base class for managing id attributes in other classes.

"""


class Base:
    """
    This class manages the id attribute for its subclasses.
    If an id is provided during initialization, it assigns
    that id to the instance. Otherwise, it increments a class-level
    counter and assigns the new value to the instance.

    Attributes:
        __nb_objects: A private class attribute to track the number
            of objects created.
        id: The public instance attribute representing the object's
            identifier.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance with an id.

        Args:
            id: The identifier for the object. If None, a new id is generated.
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
