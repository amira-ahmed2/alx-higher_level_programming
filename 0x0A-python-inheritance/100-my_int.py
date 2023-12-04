#!/usr/bin/python3
"""Write a class MyInt that inherits from int"""


class MyInt(int):
    """Write a class MyInt that inherits from int"""
    def __eq__(self, value):
        return(self.real != value)
    
    def __ne__(self, value):
        return super().__eq__(value)
        