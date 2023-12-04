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

    def area(self):
        """ the area Square
        """
        return self.__size * self.__size

    def __str__(self):
        """print() should print, and str() should return"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
