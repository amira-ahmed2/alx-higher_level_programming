#!/usr/bin/python3
"""To JSON string"""
import json


def from_json_string(my_str):
    """from json str

    Args:
        my_str (_type_): _description_
    """
    return json.loads(my_str)
