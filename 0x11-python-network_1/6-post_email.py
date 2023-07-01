#!/usr/bin/python3
"""Sends POST request to URL with email as a parameter. Display response"""
import requests
import sys


if __name__ == "__main__":
    req = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(req.text)
