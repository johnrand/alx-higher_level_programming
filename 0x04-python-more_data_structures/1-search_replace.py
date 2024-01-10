#!/usr/bin/python3

"""
    search_replace:
        function that replaces all occurences of an element by
        another in a new list
    my_list:
        initial list
    search:
        the element to replace
    replace:
        new element
"""


def search_replace(my_list, search, replace):
    nlist = [replace if element == search else element for element in my_list]
    return nlist
