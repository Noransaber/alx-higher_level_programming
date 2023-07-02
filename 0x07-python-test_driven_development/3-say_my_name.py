#!/usr/bin/python3
"""Define say my name function"""


def say_my_name(first_name, last_name=""):
    """Say the first and last name

    Args:
        firrst and last names
    Raises:
        TypeError: if the last and first name
        is not string
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
