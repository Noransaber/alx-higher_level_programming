#!/usr/bin/python3
"""Define a class"""


class Square:
    """Represent a class"""

    def __init__(self, size=0):

        self.size = size

    @property
    def size(self):
        """Get/set the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(sef):
        """return the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with #"""
        for n in range(0, self.__size):
            [print("#", end="") for k in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
