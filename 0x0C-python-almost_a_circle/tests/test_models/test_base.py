#!/usr/bin/python3
""" Test Base Model"""
from models.base import Base
from unittest import TestCase
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
import unittest


class TestBaseMethods(unittest.TestCase):
    """ BASE CLASS TESTING"""

    def setUp(self):
        """ EACH TEST METOD TESING """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ ID TESTING """
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        """ ID TESTING """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        """ NB OBJ ATTR TESTING"""
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mix(self):
        """ NB IBJ ATTR AND IS TESTING"""
        new = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1024)
        self.assertEqual(new3.id, 2)

    def test_string_id(self):
        """ ID STR TESTING"""
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args_id(self):
        """ MORE THAN ONE ARG PASSING TESTING """
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        """ ACCESSING PRIVATE ATTR TESTING"""
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file_1(self):
        """ Test JSON file """
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ KSON FILE TESTING"""
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
