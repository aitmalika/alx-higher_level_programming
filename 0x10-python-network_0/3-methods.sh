#!/bin/bash
# script that takes in a URL and displays all HTTP methods this server will accept
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
