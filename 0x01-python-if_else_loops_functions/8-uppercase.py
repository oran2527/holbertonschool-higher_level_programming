#!/usr/bin/python3
def uppercase(str):
    for x in range(0, len(str)):
        let = ord(str[x])
        if ord(str[x]) >= 97 and ord(str[x]) <= 122:
            let = let - 32
        print(chr(let), end="")
    print()
