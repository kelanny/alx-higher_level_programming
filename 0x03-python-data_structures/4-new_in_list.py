#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """Replaces an elem in a list at a specific index without changing orig."""
    if idx < 0:
        return my_list[:]
    if idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
