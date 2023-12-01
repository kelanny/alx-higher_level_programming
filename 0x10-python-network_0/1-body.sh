#!/bin/bash
# send a GET request to the provided URL, and displays the body of the response
curl -sL -w "%{http_code}" "$1" -o /dev/null --max-redirs 0
