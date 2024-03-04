#!/bin/bash
# script that takes in a URL, sends a POST request to this passed URL, and displays this body of the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
