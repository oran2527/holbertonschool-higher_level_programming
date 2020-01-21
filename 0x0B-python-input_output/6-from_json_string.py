#!/usr/bin/python3
import json
""" Module point 6

    Description: Convert json to python
    Return: python object"""


def from_json_string(my_str):
    """from_json_string"""

    new_p = json.loads(my_str)
    return new_p
