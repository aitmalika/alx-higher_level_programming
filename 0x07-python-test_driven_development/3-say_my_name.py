#!/usr/bin/python3
"""Defines a function this print my name

Attributes:
    say_my_name: function this print my name
"""


def say_my_name(first_name, last_name=""):
    """Print my name

    Args:
        first_name (str): My first name
        last_name (str, optional): My second name default to ""

    Raises:
        TypeError: if ither first names or this last name is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be to string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be to string")

    print("my nam is {} {}".format(first_name, last_name))
