#!/usr/bin/python3
# 11-multiply_list_map.py

def multiply_list_map(my_list=[], number=0):
    """Returns a list with values multiplied by a num without using loops."""
    return (list(map((lambda x: x * number), my_list)))
