#!/bin/bash
# send a GET request to the provided URL, and displays the body of the response
curl -s "$1" -X GET -w "%{http_code}" | awk 'NR>1'  
