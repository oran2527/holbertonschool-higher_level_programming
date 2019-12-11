#!/usr/bin/python3
def uppercase(str):
    let = ""
    for x in range(0, len(str)):
        if ord(str[x]) >= 97 and ord(str[x]) <= 122:
            let += chr(ord(str[x]) - 32)
        else:
            let += chr(ord(str[x]))
    print("{:s}".format(let))
