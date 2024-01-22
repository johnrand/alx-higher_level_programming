#!/usr/bin/python3

"""
    Execute a function safely

    Args:
    fct - the function to execute
    *args - arguments to be passed to function

    Return:
    The result of the function
"""


def safe_function(fct, *args):
    try:
        fct_result = fct(*args)
        return fct_result
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
