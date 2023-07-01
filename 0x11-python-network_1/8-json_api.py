#!/usr/bin/python3
"""send POST request with letter as a parameter."""
import requests
import sys


if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    req = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        info = req.json()
        if info:
            print("[{}] {}".format(info.get("id"), info.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
