#!/usr/bin/python3

def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple."""
    if not my_list:
        return (0)
    number = 0
    wght = 0

    for tupl in my_list:
        number += tupl[0] * tupl[1]
        wght += tupl[1]
    return (number / wght)
