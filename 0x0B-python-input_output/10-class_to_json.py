#!/usr/bin/python3
import json
""" Module point 10

    Description: Class to Json
    Return: data structure"""


def class_to_json(obj):
    """class_to_json function"""
    return obj.__dict__
