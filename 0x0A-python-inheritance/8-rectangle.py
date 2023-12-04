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
