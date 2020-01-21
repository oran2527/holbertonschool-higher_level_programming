#!/usr/bin/python3
import json
""" Module point 5

    Description: Convert python to json
    Return: json"""


def to_json_string(my_obj):
    """append_write"""

    new_j = json.dumps(my_obj, sort_keys=True)
    return new_j
