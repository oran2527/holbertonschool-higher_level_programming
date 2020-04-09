#!/bin/bash
# point 8 post json file
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
