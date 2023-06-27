#!/usr/bin/python3
"""Define a class"""


class Square:
    """Represent the class"""

    def __init__(self, size=0):
        """init a new aquare"""

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Return square area"""
        return (self.__size * self.__size)
