#!/usr/bin/python3
"""ModuleComment"""

if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, password))
    print(r.json().get('id'))
