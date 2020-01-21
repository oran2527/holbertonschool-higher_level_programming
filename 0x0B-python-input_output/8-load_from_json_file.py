#!/usr/bin/python3
import json
""" Module point 8
    Description: Create an object from a json
    Return: a python object"""


def load_from_json_file(filename):
    """load_from_json_file"""
    with open(filename, 'r') as f:
        return json.load(f)
