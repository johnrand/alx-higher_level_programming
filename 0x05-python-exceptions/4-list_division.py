#!/usr/bin/python3

"""
    Divide element by element of two lists.

    Args:
    my_list_1 - the first input list
    my_list_2 - the second input list
    list_length - new list of any legnth > the 1 and 2 list

    Return:
    new_list with all the divisions
"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                div_res = my_list_1[i] / my_list_2[i]
                new_list.append(div_res)
            except (ZeroDivisionError, TypeError):
                new_list.append(0)
                if isinstance(my_list_1[i], (int, float)) and
                isinstance(my_list_2[i], (int, float)):
                    if isinstance(my_list_1[i], str) or
                    isinstance(my_list_2[i], str):
                        print("wrong type")
                    else:
                        print("division by 0")
                    else:
                        print("wrong type")
    except IndexError:
        print("out of range")
    finally:
        return new_list
