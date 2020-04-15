#!/usr/bin/python3
''' point 1 X-Request-Id requests '''

if __name__ == "__main__":

    import requests
    import sys

    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
