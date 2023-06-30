#!/bin/bash
# This script takes in a URL, sends a DELETE requests to the URL.
curl -s -X "DELETE" $1
