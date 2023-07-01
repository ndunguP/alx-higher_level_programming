#!/usr/bin/python3
"""Fetches a URL using request. Display value of variable X-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers.get("X-Request-Id"))
