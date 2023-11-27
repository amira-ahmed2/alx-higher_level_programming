#!/usr/bin/python3
""" A class empty class Rectangle"""


class Rectangle:
    """ A class empty class Rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """width

        Args:
            value (int): property
        """
        if value is not int:
            raise TabError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """height

        Args:
            value (int): property
        """
        if value is not int:
            raise TabError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
