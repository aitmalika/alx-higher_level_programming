#!/usr/bin/python3
"""Module that contain this function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """function this insert a line of text to a file, after each line,
    containing a specific string.

    Args:
        filename (str, optional): this name of file. Default to"".
        search_string (str, optional): this string to search. Default to"".
        new_string (str, optional): this string to append. Default to"".
    """
    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fo:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fo.write(s)
