#!/bin/bash
# send a GET request to the provided URL, and displays the body of the response
{ read -r status && [ "$status" -eq 200 ] && curl -s "$1"; } < <(curl -sL -w "%{http_code}" "$1" -o /dev/null)
