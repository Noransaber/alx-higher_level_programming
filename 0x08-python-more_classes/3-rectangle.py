#!/usr/bin/python3
"""Class retangel"""


class Rectangle:
    """Define a class"""

    def __init__(self, width=0, height=0):
        """Init a new retangle
        Args:
        width: int
        height: init

        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError(" width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return the area of the retangel"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the retangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the pritable representation of the retangle
        represent retangel with #
        """
        if self.__width == 0 or self.__height == 0:
            return("")

        r = []
        for i in range(self.__height):
            [r.append('#') for k in range(self.__width)]
            if i != self.__height - 1:
                r.append("\n")
        return ("".join(r))
