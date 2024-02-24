#!/usr/bin/python3

"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from dynamically new instance attributes
    except if attributes is called 'first_name'.
    """

    __slots__ = ["first_name"]
