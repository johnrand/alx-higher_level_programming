#!/usr/bin/python3

"""
    common_elements:
        function that returns a set of common elements in two sets
    set_1 and set_2:
        the sets
"""


def common_elements(set_1, set_2):
    common_set = {element for element in set_1 if element in set_2}

    return common_set
