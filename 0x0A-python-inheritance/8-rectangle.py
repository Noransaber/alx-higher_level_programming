#!/usr/bin/python3
"""Define a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """init class retangle"""

    def __init__(self, width, height):
        """init new retngle
        Args:
        width and height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
