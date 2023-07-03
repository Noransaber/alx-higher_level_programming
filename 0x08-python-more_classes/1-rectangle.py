#!/usr/bin/python3
"""Class Retangle"""


class Rectangle:
    """ Init class retangle"""

    def __init__(self, width=0, height=0):
        """New Retangle

        Args:
            Width = type int and it's the width of it
            Height = int and ithe the heigh
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set/Update the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
