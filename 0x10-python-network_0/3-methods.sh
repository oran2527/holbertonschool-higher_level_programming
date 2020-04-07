#!/bin/bash
# show all methods in the server
req="$(curl -sI -X OPTIONS 0.0.0.0:5000)"; mt=$(echo "$req" | grep Allow); echo "${mt/Allow: /}"
