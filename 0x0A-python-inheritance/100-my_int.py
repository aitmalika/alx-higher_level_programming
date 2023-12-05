#!/usr/bin/python3
"""Define this class MyInt that inherit from int"""


class MyInt(int):
    """Invert int operator == and !="""

    def __eq__(self, value):
        """Override == operator with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior"""
        return self.real == value
