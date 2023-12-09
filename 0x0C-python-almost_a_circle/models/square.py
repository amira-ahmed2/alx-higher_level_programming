#!/usr/bin/python3
"""class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square

    Args:
        Rectangle (class): inheart there
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """sets size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """_summary_
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v


    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y
        }
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
