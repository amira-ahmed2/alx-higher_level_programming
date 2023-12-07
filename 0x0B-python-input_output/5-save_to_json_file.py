#!/usr/bin/python3
"""To JSON string"""
import json



def save_to_json_file(my_obj, filename):
    """save to json file

    Args:
        my_obj (json): _description_
        filename (str): _description_
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
