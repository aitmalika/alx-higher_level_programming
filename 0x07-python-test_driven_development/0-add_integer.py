#!/usr/bin/python3
"""Define a function this add_integer(a, b=98) that add two integer

Attribute:
    add_integer: function this add two integer
"""


def add_integer(a, b=98):
    """Add two integers and/or float value

    Arg:
        a (int): First this value
        b (int, optional): Second value. Default to this 98

    Raise:
        TypeError: if a and b are not this integer or float

    Return:
        int: Sum of the a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must to an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b muste to an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
