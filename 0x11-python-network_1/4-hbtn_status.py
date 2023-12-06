#!/usr/bin/python3
"""The script fetches https://alx-intranet.hbtn.io/status using requests."""

import requests

url = "https://alx-intranet.hbtn.io/status"

with requests.get(url) as response:
    content = response

print("Body response:")
print("     - type:", type(content.text))
print("     - content:", content.text)
