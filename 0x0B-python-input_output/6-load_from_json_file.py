#!/usr/bin/python3
"""Define a function"""
import json


def load_from_json_file(filename):
    """Function creates an Object from a “JSON file"""
    with open(filename) as f:
        return json.load(f)
