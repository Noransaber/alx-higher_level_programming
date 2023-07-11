#!/usr/bin/python3
"""Define a class"""


class Student:
    """Start a new class"""

    def __init__(self, first_name, last_name, age):
        """init a new class
        Args:
        firstname: string
        lastname: string
        age: int
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return describtion about the class"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {n: getattr(self, n) for n in attrs if hasattr(self, n)}
        return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
