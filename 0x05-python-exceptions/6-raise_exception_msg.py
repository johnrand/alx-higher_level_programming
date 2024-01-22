#!/usr/bin/python3

"""
    Funtion that Raises a name exception with a message

    Args:
    message - a string message

    Raise:
    NameError - always raise name exception
"""


def raise_exception_msg(message=""):
    raise NameError(message)
