#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    r = r.text
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))
