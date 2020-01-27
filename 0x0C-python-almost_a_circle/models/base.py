#!/user/bin/python3
import json
""" module point 1 base class """


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string function"""
        if list_dictionaries is None:
            return
        else:
            new_j = json.dumps(list_dictionaries, sort_keys=True)
            return new_j
