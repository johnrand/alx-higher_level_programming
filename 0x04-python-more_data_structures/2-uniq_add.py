#!/usr/bin/python3

"""
    uniq_add:
        function that adds all unique integers in a list
        (only once for each integer).
    my_list:
        the list
"""


def uniq_add(my_list):
    uniq_set = set()
    total = 0

    for integer in my_list:
        if integer not in uniq_set:
            total += integer
            uniq_set.add(integer)

    return total
