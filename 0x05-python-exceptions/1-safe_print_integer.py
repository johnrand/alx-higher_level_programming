#!/usr/bin/python3

"""
    Print an integer with {:d}.format()

    Args:
    Value - the input value

    Return:
    bool - True if value is correctly printed as integer else False
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
