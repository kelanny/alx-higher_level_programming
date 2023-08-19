#!/usr/bin/python3
# 9-multiply_by_2.py

def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2."""
    new_dict = {}
    for key in a_dictionary.keys():
        new_dict[key] = a_dictionary[key] * 2
    return (new_dict)
