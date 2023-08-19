#!/usr/bin/python3
# 3-common_elements.py

def common_elements(set_1, set_2):
    new_common_set = set()
    for el in set_1:
        if el in set_2:
            new_common_set.add(el)
    return (new_common_set)
