#!/usr/bin/python3

"""
    update_dictionary:
        function that replaces or adds key/value in a dictionary
    a_dictionary:
        the dictionay
    key:
        argument will be always a string
    value:
        argument will be any type
"""


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
