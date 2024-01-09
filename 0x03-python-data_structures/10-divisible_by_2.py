#!/usr/bin/python3

"""
    divisible_by_2:
                    A function that returns True if an integer in a list
                    is multiple of 2 else returns False

    my_list[]:
                The list to be checked

"""


def divisible_by_2(my_list=[]):
    result = [number % 2 == 0 for number in my_list]
    return result
