#!/usr/bin/python3
"""
    max_integer:
        find biggest integer in a list
    my_list:
        list to iterate through
"""


def max_integer(my_list[]):
    if not mylist:
        return None

    biggest = my_list[0]
    for i in my_list:
        if i > biggest:
            biggest = i

    return biggest
