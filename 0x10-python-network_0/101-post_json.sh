#!/bin/bash
# script that sends a JSON POST request to a URL passed as this first argument, and displays this body of the response.
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
