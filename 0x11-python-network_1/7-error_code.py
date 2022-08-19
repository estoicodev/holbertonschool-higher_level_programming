#!/usr/bin/python3
"""
Sends a request to the URL and displays the body
of the response decoded in utf-8 (with requests module)
Manage HTTPError displaying the status code
"""

if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
