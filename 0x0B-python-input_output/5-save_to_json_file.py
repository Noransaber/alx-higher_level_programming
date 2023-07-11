#!/usr/bin/python3
"""Define a function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file
    using a JSON representation"""
    with open(filename, mode="w") as myF:
        json.dump(my_obj, filename)
