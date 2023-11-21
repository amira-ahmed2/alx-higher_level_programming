#!/usr/bin/python3
"""defines class Square """


class Square:
    """Represents a square
    Attributes:
        __size (int): size of  the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """init square
        Args:
            size (int): size of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """position of the square
        Returns:
        tulb: position of Square
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """that prints in
        stdout the square with the character #
        """
        if self.__size == 0:
            print()

        for ii in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for a in range(0, self.__size):
                print("#", end="")
            print("")
