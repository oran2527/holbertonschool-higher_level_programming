#!/bin/bash
# show all methods in the server
curl -sI -X OPTIONS "$1" | grep -i Allow | cut --complement -d ' ' -f 1
