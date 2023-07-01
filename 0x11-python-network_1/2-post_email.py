#!/usr/bin/python3
"""Sends a POST request to URL with email as a parameter"""
import urllib.request
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        page = response.read()

    print(page.decode('utf-8'))
