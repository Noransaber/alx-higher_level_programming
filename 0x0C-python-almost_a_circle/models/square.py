#!/usr/bin/python3
"""Define a square"""
from models.rectangle import Rectangle


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
        super().__init__(size, size, x, y, id)

    
    def __str__(self):
        """ str special method """
        str_s = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_w = "{}/{}".format(self.width, self.height)

        return str_s + str_id + str_xy + str_w

    @property
    def size(self):
        """Return the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Update the size"""
        self.width = value
        self.height = value

    def __str__(self):
        """ str special method """
        str_rectangle = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_rectangle + str_id + str_xy + str_size

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
        if args is not None and len(args) != 0:
            lst_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if lst_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, lst_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key ,value)

    def to_dictionary(self):
        """Return the dic repreof the  square"""
        lst_atr = ['id', 'size', 'x', 'y']
        dict_re = {}

        for key in lst_atr:
            if key == 'size':
                dict_re[key] = getattr(self, 'width')
            else:
                dict_re[key] = getattr(self, key)

        return dict_re
