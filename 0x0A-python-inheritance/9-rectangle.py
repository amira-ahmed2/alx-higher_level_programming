#!/usr/bin/python3
"""class rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this is an class"""
    def __init__(self, width, height):
        """intialize Rectangle

        Args:
            width (int): _description_
            height (int): _description_
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ the area Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """print() should print, and str() should return"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
