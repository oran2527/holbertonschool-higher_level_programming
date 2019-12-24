#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        a_dictionary.update({key: value})
        return a_dictionary
    for i in a_dictionary.copy():
        if i == key:
            a_dictionary.update({i: value})
        else:
            a_dictionary.update({key: value})
    return a_dictionary
