#!/usr/bin/python3
""" Define a function"""


def append_after(filename="", search_string="", new_string=""):
    """ insert a text after each line
    Args
    filename (str)
    searching_string (str)
    new_string (str)
    """
    txt = ""
    with open(filename) as f:
        for ln in f:
            txt += ln
            if search_string in ln:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
