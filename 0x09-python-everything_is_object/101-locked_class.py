#!/usr/bin/python3


class LockedClass:
    def __setattr__(self, name, value):
        if name != "first_name":
            msg = "'LockedClass' object has no attribute "
            raise AttributeError("{} '{}'".format(msg, name))
        super().__setattr__(name, value)
