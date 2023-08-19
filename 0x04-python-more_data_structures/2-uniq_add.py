#!/usr/bin/python3
# 2-uniq_add.py

def uniq_add(my_list=[]):
    unique_list = set(my_list)
    total = 0
    for i in unique_list:
        total += i
    return (total)
