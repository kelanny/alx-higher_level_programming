#!/usr/bin/python3
# 12-fizzbuzz.py
def fizzbuzz():
    """Prints the numbers 1-100 separated by space."""
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 3 == 0 and i % 5 == 0:
            print("FIzzBuzz", end=" ")
        else:
            print(i, end=" ")
