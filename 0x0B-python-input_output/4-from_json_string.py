#!/usr/bin/python3

"""
4-from_json_string.py - module of a functio that returns an
object (Python data structure) represented by a JSON string.

"""


import json


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure)
    represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        object: The Python data structure represented by the JSON string.

    Raises:
        None
    """
    return json.loads(my_str)
