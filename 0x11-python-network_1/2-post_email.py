#!/usr/bin/python3
''' point 2 get email urllib '''


if __name__ == "__main__":

    from urllib import request, parse
    import sys

    data = parse.urlencode({'email': sys.argv[2]}).encode()
    req = request.Request(sys.argv[1], data=data, method='POST')
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
