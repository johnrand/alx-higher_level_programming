#!/usr/bin/python3

"""
    complex_delete:
        function that deletes keys with a specific value in a dictionary.
    a_dictionar:
        the dictionary to work on
    value:
        value associated with the key
"""


def complex_delete(a_dictionary, value):
    key_delete = [key for key, val in a_dictionary.items() if val == value]
    for key in key_delete:
        del a_dictionary[key]
    return a_dictionary
