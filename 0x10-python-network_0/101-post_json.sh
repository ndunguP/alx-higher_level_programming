#!/bin/bash
# This script sends a JSON POST request to a URL.
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"
