#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter (with requests module)
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 1:
        letter = {'q': ''}
    elif len(sys.argv) == 2:
        letter = {'q': sys.argv[1]}

    r = requests.post('http://0.0.0.0:5000/search_user', data=letter)

    try:
        r_json = r.json()
        if r_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(r_json.get('id'), r_json.get('name')))
    except (ValueError, requests.exceptions.JSONDecodeError):
        print("Not a valid JSON")
