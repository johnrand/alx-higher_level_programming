#!/usr/bin/python3

"""
    multiply_by_2:
        function that returns a new dictionary with all values
        multiplied by 2
    a_dictionary:
        the dictionay
"""


def multiply_by_2(a_dictionary):
    new_dictionary = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dictionary
