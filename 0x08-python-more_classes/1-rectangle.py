#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """this represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        Args:
            width:width of the rectangle
            height:height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """gets width attribute"""
        return self.width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        """get height attribute"""
        return self.height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value
