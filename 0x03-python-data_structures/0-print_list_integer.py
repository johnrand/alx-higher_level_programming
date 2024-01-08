#!/usr/bin/python3

"""
    print_list_integer:
                        function to print integers in a list
    my_list:
            list to be printed
"""


def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))
