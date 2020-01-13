#!/usr/bin/python3
"""say_my_name - print a name

   Description: return a string with the name
   Return: name according variables
"""


def say_my_name(first_name, last_name=""):
    """say_my_name - function.
       first_name - first value.
       last_name - second value."""
    if type(first_name) is str and type(last_name) is str:
        print("My name is {:s} {:s}".format(first_name, last_name))
    if type(first_name) is not str and type(last_name) is not str:
        raise TypeError("first_name must be a string\
\nlast_name must be a string")
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
            raise TypeError("last_name must be a string")
