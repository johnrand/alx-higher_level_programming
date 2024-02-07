#!/usr/bin/python3

"""
6-load_from_json_file.py - A module for a function that
creates an Object from a “JSON file”.

"""

import json


def load_from_json_file(filename):
    """
    Function that creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load the object from.

    Returns:
        object: The Python data structure represented by the JSON file.

    Raises:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
