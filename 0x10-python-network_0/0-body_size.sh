#!/bin/bash
# Check if the URL is provided as an argument

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request using curl and display the body if the status code is 200
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
