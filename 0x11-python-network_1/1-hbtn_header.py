#!/usr/bin/python3
"""fetch URL module using command line argument"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = dict(response.info())

    print(html.get("X-Request-Id"))
