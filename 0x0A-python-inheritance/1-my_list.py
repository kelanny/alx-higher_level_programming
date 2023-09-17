#!/usr/bin/python3
# 1-my_list.py
"""
This module contain one class MyList that inherits from list.
"""


class MyList(list):
    """A class representation that expands the built in list class.
    """
    def print_sorted(self):
        """Prints a sorted list(Ascending order).
        """
        print(sorted(self))
