#!/bin/bash
# This script sends a request to a URL. Displays the status code of response
curl -s -o /dev/null -w '%{http_code}' $1
