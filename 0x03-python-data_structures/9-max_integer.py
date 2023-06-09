#!/usr/bin/python3
""" finds the biggest integer of a list."""


def max_integer(my_list=[]):
    if my_list == 0:
        return None

    Lnum = my_list[0]
    for num in my_list:
        if Lnum < num:
            Lnum = num
    return Lnum
