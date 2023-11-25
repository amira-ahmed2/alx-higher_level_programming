#!/usr/bin/python3
"""Module that prints a text with 2 new lines after
"""


def text_indentation(text):
    """that prints a text with 2 new lines after
    each of these characters: ., ? and :
    Args:
        text (str): str
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    special_char = ['.', '?', ':']
    for i in text:
        print(i, end='')
        if i in special_char:
            print("\n\n", end='')
