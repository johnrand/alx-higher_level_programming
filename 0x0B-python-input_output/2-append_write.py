#!/usr/bin/python3

"""
2-append_write.py - A module with a function that appends a string
at the end of a text file

"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and
    returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.

    Raises:
        None
    """

    chars_added = 0
    with open(filename, 'a', encoding='utf-8') as file:
        chars_added = file.write(text)
    return chars_added
