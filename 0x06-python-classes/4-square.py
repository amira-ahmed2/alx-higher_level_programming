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
        self.__size = size

    def area(self):
        """get area Square
        Returns:
        int: size area of Square
        """
        return self.__size ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
        int: size area of Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of size

        Args:
            value (int): size
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
