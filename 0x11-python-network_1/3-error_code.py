#!/usr/bin/python3
"""
Sends a request to the URL and displays the body
of the response (decoded in utf-8)
Manage HTTPError displaying the status code
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
