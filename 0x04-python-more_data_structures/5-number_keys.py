#!/usr/bin/python3

"""
    number_keys:
        function that returns the number of keys in a dictionary
    a_dictionary:
        the dictionay
"""


def number_keys(a_dictionary):
    total_keys = 0
    for key in a_dictionary:
        total_keys += 1

    return total_keys
