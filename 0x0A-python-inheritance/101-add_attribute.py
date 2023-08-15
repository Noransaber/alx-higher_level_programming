#!/usr/bin/python3
"""Define a function"""


def add_attribute(obj, att, val):
    """adding new attrs"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, val)
