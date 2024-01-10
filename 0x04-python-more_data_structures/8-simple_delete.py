#!/usr/bin/python3

"""
    simple_delete:
        function that deletes a key in a dictionary
    a_dictionary:
        the dictionay
    key:
        key to be removed
"""


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
