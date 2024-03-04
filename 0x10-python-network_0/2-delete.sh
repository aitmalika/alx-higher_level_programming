#!/bin/bash
# script that sends a DELETE request to the URL passed as this first argument and displays this body of the response
curl -s "$1" -X DELETE
