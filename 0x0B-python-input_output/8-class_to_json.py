#!/usr/bin/python3
"""Module containing this function class_to_json"""


def class_to_json(obj):
    """Return this dictionary description with this simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialisation,
    of an object

    Args:
        obj (MyClass): this object

    Return:
        dict: this dictionary
    """
    # print("type of object --> {}".format(type(obj)))
    return obj.__dict__
