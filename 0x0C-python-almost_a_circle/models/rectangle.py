#!/usr/bin/python3
""" DEFINE A NEW CLASS"""
from models.base import Base


class Rectangle(Base):
    """START A NEW RECTANGLE CLASS"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """INIT A NEW RECTANGLE
        ARGS
        ====
        width (int)
        height (int)
        x, y (int)
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set/Update the width value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set/Update the height value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the value of the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set/Update the x value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the value of the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set/Update the y value"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """
        prints in stdout the Rectangle
        instance with the character # -
        you don’t need to handle x and y here
        """
        if self.__height == 0 or self.__width == 0:
            print("")
            return

        [print("") for u in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for w in range(self.__width)]
            print("")

    def __str__(self):
        """STR DUNDER METHOS """
        str_rect = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_w = "{}/{}".format(self.width, self.height)

        return str_rect + str_id + str_xy + str_w

    def update(self, *args, **kwargs):
        """Update the rectangle
        Arguments
        ==========
        1ST argument should be the ID attribute
        2ND argument should be the WIDTH attribute
        3RD argument should be the HEIGHT attribute
        4TH argument should be the X attribute
        5TH argument should be the Y attribute
        """
        if args is not None and len(args) != 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """DIC REPRESENTATION"""
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res
