#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    params = {
        "email": sys.argv[2]
    }

    query_string = urllib.parse.urlencode(params)
    data = query_string.encode("ascii")

    with urllib.request.urlopen(sys.argv[1], data) as response:
        body = response.read()
        print(body.decode('utf-8'))
