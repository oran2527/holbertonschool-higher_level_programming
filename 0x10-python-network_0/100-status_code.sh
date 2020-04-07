#!/bin/bash
# point 7 get the status code
curl --write-out "%{http_code}\n" --silent --output /dev/null "$1"
