#!/usr/bin/python3
"""Class Retangle"""


class Rectangle:
    """Define a class retangle"""

    def __init__(self, width=0, height=0):
        """ Init a new retangle
        Args:
        Width: type integer
        Height: Type integer

        Rasie: TypeError if not int
        ValueError: if negative
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set OR Update the value of the width"""
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
        """Set the value of  the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
