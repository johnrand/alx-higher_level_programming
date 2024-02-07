#!/usr/bin/python3

"""
5-save_to_json_file.py - module of a function that writes an
Object to a text file, using a JSON representation.

"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be saved to the file.
        filename (str): The name of the file to save the object to.

    Returns:
        None

    Raises:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
