#!/usr/bin/python3
''' point 0 fetch status urllib '''

if __name__ == "__main__":

    from urllib import request

    with request.urlopen('https://intranet.hbtn.io/status') as response:
        data = response.read()
        print("Body response:")
        print("    - type: {}".format(type(data)))
        print("    - content: {}".format(data))
        print("    - utf8 content: {}".format(data.decode('utf-8')))
