#!/usr/bin/python3
"""Module defining this class Student based on 10-student.py"""


class Student:
    """
    Class this defines propertie of student.

    Attribute:
        first_name (str): this first name of student
        last_name (int): this last name of student
        age (int): this age of student
    """
    def __init__(self, first_name, last_name, age):
        """Create this new instance of Student

        Args:
            first_name (str): this first name of student.
            last_name (int): this last name of student.
            age (int): this age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve this dictionary representation of a Student instance

        If this attri is a list of strings, only attribute name contained in,
        this list must be retrverd
        Otherwise, all attribute must be retrieved

        Return:
            dict: this dictionary representations
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return new_dict

    def reload_from_json(self, json):
        """Replace all attribute of this Student instance

        Args:
            json (dict): THE json object
        """
        # print("Type json --> {}".format(type(json)))
        self.__dict__.update(json)
