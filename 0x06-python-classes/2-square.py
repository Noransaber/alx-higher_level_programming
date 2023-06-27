#!/usr/bin/python3
"""Deine a class"""


class Square:
    """Represent the square"""

    def __init__(self, size=0):
        """initalize a new square"""

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
