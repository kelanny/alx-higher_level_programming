#!/usr/bin/python3
# 6-print_sorted_dictionary.py

def print_sorted_dictionary(a_dictionary):
    """Print a dictinary sorted by keys."""
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary.get(key)))
