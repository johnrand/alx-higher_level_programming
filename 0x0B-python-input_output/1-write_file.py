#!/usr/bin/python3

"""
0-read_file.py - A module for writting text into filename
and returns the number of character written

"""


def write_file(filename="", text=""):
    """
    Writes a string to text file (UTF8) and returns
    number of characters.

    Args:
        filename (str): The name of the file to write.
        text (str): string to write

    Returns:
        int: Number of characters

    Raises:
        None
    """

    char_written = 0
    with open(filename, 'w', encoding='utf-8') as file:
        char_written = file.write(text)
    return char_written
