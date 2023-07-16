#!/usr/bin/python3
"""Define a class"""
import json


class Base:
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
            self.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string
        representation of list_dictionaries:
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string
        representation of list_objs
        to a file:
        """
        filename = cls.__name__ + ".json"
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
        if json_string is None or json_string == []:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with
        all attributes already set:
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        fn = str(cls.__name__) + ".json"
        try:
            with open(fn, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
        except Exception:
            return []
