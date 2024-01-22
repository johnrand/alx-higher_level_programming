#!/usr/bin/python3

"""
    function that does what a bytcode does
"""


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except Exception as e:
            result = b + a
            break

    return result
