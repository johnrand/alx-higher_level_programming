#!/usr/bin/python3

"""
100-append_after.py - Module to appand after a searched string

"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line
    containing a specific string.

    Args:
        filename (str): The name of the file to insert the new string into.
        search_string (str): The specific string to search for in each line.
        new_string (str): The line of text to insert after each line
        containing the search string.

    Returns:
        None

    Raises:
        None
    """
    with open(filename, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()
