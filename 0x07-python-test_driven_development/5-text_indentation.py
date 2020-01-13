#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    if type(text) is str:
        for x in range(0, len(text)):
            print(text[x], end="")
            if text[x] is "." or text[x] is "?" or text[x] is ":":
                print("\n")
