#!/usr/bin/python3
"""Define new classs"""


class MyList(list):
    """Start a new class inherit from the super one"""

    def print_sorted(self):
        print(sorted(self))
