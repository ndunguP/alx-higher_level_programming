#!/bin/bash
# This script takes a URL and sends a response. Dispalys the size of the body
curl -si $1 | grep "Content-Length: " | cut -d ' ' -f 2
