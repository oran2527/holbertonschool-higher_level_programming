#!/usr/bin/python3
''' point 3 error urllib '''


if __name__ == "__main__":

    from urllib import request, parse, error
    import sys

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
