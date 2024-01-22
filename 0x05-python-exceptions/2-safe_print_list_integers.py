#!/usr/bin/python3

"""
    Print first x integers of a List.

    Args:
    my_list - the input list.
    x - The number of elements to access.

    Return:
    The real number of integers printed.
"""


def safe_print_list(my_list=[], x=0):
    count_print = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count_print += 1
    except (IndexError, ValueError):
        pass

    print()
    return count_print
