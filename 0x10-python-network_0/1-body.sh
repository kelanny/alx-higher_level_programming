#!/bin/bash
# send a GET request to the provided URL, and displays the body of the response
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

response=$(curl -sL -w "%{http_code}" "$1" -o /dev/null)
status="${response: -3}"

if [ "$status" -eq 200 ]; then
	curl -sL "$1"
fi
