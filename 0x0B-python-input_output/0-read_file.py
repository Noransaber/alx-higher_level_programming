#!/usr/bin/python3
"""Define a function"""


def read_file(filename=""):
    """read from file and print to
    stdout"""

    with open(filename, mode="r", encoding="utf-8") as myF:
        readF = myF.read()
        print("{}".format(readF), end="")
