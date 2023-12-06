#!/usr/bin/python3
"""Module containing this function write file"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return this number
    of character writen

    Args:
        filename (str, optional): name of this file Default to "".
        text (str, optional): string of text to write this file Default to "".

    Return:
        int: this number of character writen to file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        """This method return this number of character writen to a file"""
        return f.write(text)
