#!/usr/bin/python3
"""Define a square"""


class Square(Rectangle):
    """init a square classs"""

    def __init__(self, size, x=0, y=0, id=None):
        """Make a new square
        Arguments
        =============
        size: int
        x: int
        y:int
        id: int
        """
        super().__init__(size, size, id, x, y)

    @property
    def size(self):
        """Return the size"""
        return self.width

    @size.setter
    def size_set(self, value):
        """Update the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square
         Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if arg is None:
                    self.__init__(self.size, self.x, self.Y)
                else:
                    self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self. x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dic repreof the  square"""
        return {
                "id": slef.id,
                "size": self.size
                "x": self.x
                "y": self.y
                }

    def __str__(self):
        """Return string repre of the square"""
        return "[Square] ({}) {}/{} - {}"
    .format(self.id, self.x, self.y, self.width)
