#!/usr/bin/python3
"""a function that prints all integers of a list"""


def print_list_integer(my_list=[]):
    length = len(my_list)
    for num in range(length):
        if num + 1 != length + 1:

            print("{}".format(num + 1))
