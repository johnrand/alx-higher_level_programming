#!/usr/bin/python3

"""
3-to_json_string.py - module of a function that returns the JSON
representation of an object(string)

"""


import json


def to_json_string(my_obj):
    """
    Functio Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.

    Raises:
        None
    """
    return json.dumps(my_obj)
