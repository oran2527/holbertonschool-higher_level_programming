#!/usr/bin/python3
import json
""" Module point 7
    Description: Write an object in a text file
    Return: a json file"""


def save_to_json_file(my_obj, filename):
    """save_to_json_file"""

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
