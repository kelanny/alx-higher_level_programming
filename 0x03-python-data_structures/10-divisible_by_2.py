#!/usr/bin/python3#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    new_list = [num % 2 == 0 for num in my_list]
    return new_list
