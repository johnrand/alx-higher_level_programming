#!/usr/bin/python3

"""
    print_reversed_list_integer:
        function to print integers in reverse in a list
    my_list:
        list to be printed
"""


def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
