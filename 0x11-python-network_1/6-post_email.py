#!/usr/bin/python3
''' point 6 get email requests '''


if __name__ == "__main__":

    import requests
    import sys

    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)
