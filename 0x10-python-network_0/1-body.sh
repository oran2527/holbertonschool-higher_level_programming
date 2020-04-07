#!/bin/bash
# show the body if status is 200
req="$(curl -sI "$1")"; st=$(echo "$req" | grep HTTP | awk '{print $2}'); [[ $st = '200' ]] && curl "$1" 
