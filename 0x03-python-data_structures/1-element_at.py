#!/usr/bin/python3

"""
    element_at:
        function to return an element at a given index
        and return none if the index is out of range or negative
    idx:
        index
    my_list:
        the list
"""


def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
