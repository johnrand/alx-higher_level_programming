#!/usr/bin/python3

import sys
"""
    print an integer and handle errors

    Args:
    value - the innput value

    Return:
    bool - if True value is an integer and printed correctly False otherwise
"""


def safe_print_integer_err(value):
    try:
        our_ivalue = int(value)
        print("{:d}".format(our_ivalue))
        return True
    except ValueError:
        print("Exception: ValueError", file=sys.stderr)
        return False
