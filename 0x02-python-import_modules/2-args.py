#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("0 arguments.")
if len(sys.argv) == 2:
    print("1 argument:")
    print("1: {}".format(sys.argv[1]))
if len(sys.argv) > 2:
    print("{} arguments:".format(len(sys.argv) - 1))
    for x in range(1, len(sys.argv)):
        print("{}: {}".format(x, sys.argv[x]))
