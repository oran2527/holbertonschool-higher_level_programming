#!/usr/bin/python3
''' point 1 fetch by argument urllib '''

import urllib.request
import sys

if __name__ == "__main__":
    var1 = sys.argv[1]
    with urllib.request.urlopen(var1) as response:
        print(response.getheader('X-Request-Id'))
