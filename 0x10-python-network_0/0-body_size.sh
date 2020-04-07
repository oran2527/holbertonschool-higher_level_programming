#!/bin/bash
# get the size of the http request header
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
