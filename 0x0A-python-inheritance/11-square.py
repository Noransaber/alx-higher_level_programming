#!/usr/bin/python3
"""Define a classs"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """new classs"""
    def __init__(self, size):
        """init a new class square
        Args:
            size (int)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
