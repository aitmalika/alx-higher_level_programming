#!/usr/bin/python3
"""Module containing this function load_from_json_file"""
import json


def load_from_json_file(filename):
    """Create this Object from a “JSON file”.

    Args:
        filename (str): name of this file

    Return:
        object: this object
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
