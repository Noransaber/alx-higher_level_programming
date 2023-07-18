#!/usr/bin/python3
"""Define a class"""
import json
import os.path


class Base:
    """Start a new class called base"""
    __nb_objects = 0

    def __init__(self, id=None):

        """init a new obj
         Args
         ====
         id (int)
         """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string
        representation of list_dictionaries:
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string
        representation of list_objs
        to a file:
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as jf:
            if list_objs is None:
                jf.write("[]")
            else:
                l_dics = [o.to_dictionary() for o in list_objs]
                jf.write(Base.to_json_string(l_dics))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON
        string representation
        json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        INSTANCE WITH ALL ATTR
        TO BE set:
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(10, 10)
            else:
                new = cls(10)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """ LIST OF INSTANCE"""
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        li_ins = []

        for index in range(len(list_cls)):
            li_ins.append(cls.create(**list_cls[index]))

        return li_ins
