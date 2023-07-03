#!/usr/bin/python3
"""Class retangel"""


class Rectangle:
    """Define a class"""

    def __init__(self, width=0, height=0):
        """Start a new retangle
        Args:
        width: int
        height: init

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the retangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the retangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return the area of the retangel"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the retangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the rectangle
        represent rectangel with #
        """
        if self.width == 0 or self.height == 0:
            return ""

        r = []
        for i in range(self.height):
            [r.append('#') for k in range(self.width)]
            if i != self.height - 1:
                r.append("\n")
        return "".join(r)
