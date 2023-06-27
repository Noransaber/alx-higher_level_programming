#!/usr/bin/python3
"""Deine a square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initalize a new square"""

        self.size = size

    @property
    def size(self):
        """Get/set size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area"""
        return (self.__size * self.__size)
