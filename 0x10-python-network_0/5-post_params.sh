#!/bin/bash
# This script sends a POST request and displays the body of the response
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" $1
