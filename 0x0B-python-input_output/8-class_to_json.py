#!/usr/bin/python3
"""returns the dictionary description"""


def class_to_json(obj):
    """ functioneturns the dictionary description
    with simple data structure (list, dictionary,
    string, integer and boolean) for JSON serialization
    of an object
    """
    return obj.__dict__
