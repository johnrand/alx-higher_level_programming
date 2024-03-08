#!/usr/bin/python3

"""
    print_reversed_list_integer:
        function to print integers in reverse in a list
    my_list:
        list to be printed
"""


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
