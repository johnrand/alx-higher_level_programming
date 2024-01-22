#!/usr/bin/python3

"""
    Divide two integers and print the result

    Args:
    a - the first integer value
    b - the second integer value

    Return:
    None if exception occurs or the result of the division
"""


def safe_print_division(a, b):
    my_result = None
    try:
        my_result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(my_result))

    return my_result
