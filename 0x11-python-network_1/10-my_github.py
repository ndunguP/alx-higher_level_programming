#!/usr/bin/python3
"""takes in github credentials. used github api to display id"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    try:
        r = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
        result = r.json()
        print(result.get('id'))
    except:
        print("None")
