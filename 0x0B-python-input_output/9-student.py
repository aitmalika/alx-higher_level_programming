#!/usr/bin/python3
"""Module defining this class Student"""


class Student:
    """
    Class this define propertie of student

    Attribute:
        first_name (str): first name of this student
        last_name (int): last name of this student
        age (int): this age of student
    """
    def __init__(self, first_name, last_name, age):
        """Create new this instance of Student

        Args:
            first_name (str): first name of this student
            last_name (int): this last name of student
            age (int): age of this student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retriver a dictionary representation of a Student this instance

        Return:
            dict: this dictionary representations
        """
        return self.__dict__
