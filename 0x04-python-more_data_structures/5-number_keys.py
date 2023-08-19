#!/usr/bin/python3
# 5-number_keys.py

def number_keys(a_dictionary):
    key_len = 0
    for key in a_dictionary.keys():
        key_len += 1
    return (key_len)
