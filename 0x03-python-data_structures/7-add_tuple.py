#!/usr/bin/python3
"""Write a function that adds 2 tuples."""


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a[:2] + (0, 0)
    tuple_b = tuple_b[:2] + (0, 0)

    first_ele = tuple_a[0] + tuple_b[0]
    sec_ele = tuple_b[1] + tuple_b[1]
    return (first_ele, sec_ele)


