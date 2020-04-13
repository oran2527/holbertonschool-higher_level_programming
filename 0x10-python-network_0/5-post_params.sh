#!/bin/bash
# add parameters and values method POST
curl -s -d "email=hr@holbertonschool.com1&subject=I will always be here for PLD" -X POST "$1"
