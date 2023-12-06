#!/usr/bin/python3
"""Module containing this function append_write"""


def append_write(filename="", text=""):
    """Append a string to a text file (UTF8) and return this number
    of character adde

    Args:
        filename (str, optional): name of this file Default to ""
        text (str, optional): string of text to write this file Default to""

    Return:
        int: this number of character append to file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        """This method return this number of character append to a file"""
        return f.write(text)
