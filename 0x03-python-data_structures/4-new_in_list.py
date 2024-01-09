#!/usr/bin/python3

"""
    new_in_list:
        function to replace an element at a given index
        and return new list without modifying the original list
        if the index is out of range or negative
    idx:
        index
    my_list:
        the list
    element:
        element to put in place of the replaced
"""


def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    else:
        newlist = my_list.copy
        newlist[idx] = element
        return newlist
