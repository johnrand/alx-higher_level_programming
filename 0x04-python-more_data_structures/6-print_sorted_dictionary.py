#!/usr/bin/python3

"""
    print_sorted_dictionar:
        function that prints a dictionary by ordered keys
    a_dictionary:
        the dictionay
"""


def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
