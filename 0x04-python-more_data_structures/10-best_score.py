#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        new = []
        for i in a_dictionary:
            new.append(a_dictionary.get(i))
        new.sort()
        for i in a_dictionary:
            if a_dictionary.get(i) == new[len(new) - 1]:
                return i
