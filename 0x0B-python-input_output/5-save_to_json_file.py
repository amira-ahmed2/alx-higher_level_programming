#!/usr/bin/python3
import json
"""To JSON string"""


def save_to_json_file(my_obj, filename):
    """_summary_

    Args:
        my_obj (json): _description_
        filename (str): _description_
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
