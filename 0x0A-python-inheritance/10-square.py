#!/usr/bin/python3
"""Define a class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Init a new square"""
    def __init__(self, size):
        """ init a new square
        Args:
        size (int)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
