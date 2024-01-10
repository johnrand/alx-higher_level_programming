#!/usr/bin/python3

"""
    diff_elements:
        function that returns a set of all elements
        present in only one set
    set_1 and set_2:
        the sets
"""


def diff_elements(set_1, set_2):
    diff_set = (set_1 - set_2) | (set_2 - set_1)

    return diff_set
