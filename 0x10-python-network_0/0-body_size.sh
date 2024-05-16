#!/bin/bash
# Check if the URL is provided as an argument
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
