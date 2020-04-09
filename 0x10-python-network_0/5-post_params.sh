#!/bin/bash
# add parameters and values method POST
curl -s -X POST -L "$1" -d 'email=hr@holbertonschool.com1&subject=I will always be here for PLD'
