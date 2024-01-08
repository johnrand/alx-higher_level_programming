#!/usr/bin/python3

"""
    replace_in_list:
        function to replace an element at a given index
        and return original list if the index is out of range or negative
    idx:
        index
    my_list:
        the list
    element:
        element to put in place of the replaced
"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
