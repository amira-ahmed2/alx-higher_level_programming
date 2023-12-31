#!/usr/bin/python3
"""defines class Square """


class Square:
    """Represents a square
    Attributes:
        __size (int): size of  the square
    """
    def __init__(self, size=0):
        """init square
        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
