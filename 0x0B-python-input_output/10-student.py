#!/usr/bin/python3
"""Module defining this class Student based on 9-student.py"""


class Student:
    """
    Class this define propertie of student

    Attribute:
        first_name (str): this first name of student
        last_name (int): this last name of student
        age (int): this age of student
    """
    def __init__(self, first_name, last_name, age):
        """Create new instance of this Student

        Args:
            first_name (str): this first name of student
            last_name (int): this last name of student
            age (int): this age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retriver this dictionary representation of a Student instance

        If attrs is a list of strings, only attribute names contained in
        the list must be retrieved
        Otherwise, all attribute must be retreverd

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
