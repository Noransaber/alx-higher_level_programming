#!/usr/bin/python3
"""Deines a calss"""

class MyInt(int):
    """invert int operators"""

    def __eq__(self, value):
        """Override"""
        return self.real != value

    def __ne__(self, value):
        """override"""
        return self.real == value
