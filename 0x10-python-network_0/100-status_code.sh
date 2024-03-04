#!/bin/bash 
# script that sends a request to a URL passed as an argument, and displays only this statu code of this response
curl -s -L -X HEAD -w "%{http_code}" "$1"
