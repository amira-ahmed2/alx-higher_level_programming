#!/usr/bin/python3
"""class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this is an class"""
    def __init__(self, size):
        """intialize Square

        Args:
            size (int): _description_
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
