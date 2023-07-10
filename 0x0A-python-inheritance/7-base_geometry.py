#!/usr/bin/python3
"""Define a new class"""


class BaseGeometry:
    """init a new class
    args:
    name:
    value
    """

    def area(self):
        """Raise error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
