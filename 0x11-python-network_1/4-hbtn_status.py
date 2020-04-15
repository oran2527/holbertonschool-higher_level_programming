#!/usr/bin/python3
''' point 4 status requests '''

if __name__ == '__main__':

    import requests

    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
