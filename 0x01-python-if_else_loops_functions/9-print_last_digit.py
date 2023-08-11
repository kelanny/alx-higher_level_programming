#!/usr/bin/python3
# 9-print_last_digit.py
def print_last_digit(number):
    """Returns the last digit of a number."""
    digit = abs(number) % 10
    print("{}".format(digit), end="")
    return digit
