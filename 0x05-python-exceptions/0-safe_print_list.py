#!/usr/bin/python3

"""
    Print x elements of a List.

    Args:
    my_list - the input list.
    x - The number of elements to print.

    Return:
    The real number of elements printed.
"""


def safe_print_list(my_list=[], x=0):
    count_print = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count_print += 1
    except IndexError:
        pass

    print()
    return count_print
