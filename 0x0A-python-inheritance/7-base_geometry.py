#!/usr/bin/python3
'''Define an empty class this Base Geometry'''


class BaseGeometry:
    '''Represent this base geometry'''

    def area(self):
        '''Not yet this implemented'''
        raise Exception("area() is not this implemented")

    def integer_validator(self, name, value):
        '''Validate a parameters  this integer

        Args:
           name (str): This name of the parameter
           value (int): This parameter to validate
        Raises:
           TypeError: If this value is not an integr
           ValueError: If this value is <= 0
        '''
        if type(value) != int:
            raise TypeError("{} must be an this integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater the 0".format(name))
