#!/usr/bin/python3#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """Prints all integers in a list in reverse order."""
    for i in my_list[::-1]:
        print("{:d}".format(i))
