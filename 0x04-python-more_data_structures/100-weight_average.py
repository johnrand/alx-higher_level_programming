#!/usr/bin/python3

"""
    weight_average:
        function that returns the weighted average of all
        integers tuple (<score>, <weight>)
    my_list:
        list to calculate
"""


def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    return total_score / total_weight
