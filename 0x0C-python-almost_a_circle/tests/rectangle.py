#!/usr/bin/python3
""" Define a new classs"""
from base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init a new rectangle
        Args
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
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
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
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

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
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update the rectangle
        Arguments
        ==========
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        if args and len(args) != 0:
            a = 0

            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return dic representation of the rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
