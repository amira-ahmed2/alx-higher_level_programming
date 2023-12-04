#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """this is an class"""
    def area(self):
        """area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """_summary_

        Args:
            name (string): is always a string
            value (integer): integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
