#!/usr/bin/python3
"""Define a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """init new retangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        strg = "[" + str(self.__class__.__name__) + "] "
        strg += str(self.__width) + "/" + str(self.__height)
        return strg

    def area(self):
        """return the area of the retangle"""
        return self.__width * self.__height
