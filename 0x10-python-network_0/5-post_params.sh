#!/bin/bash
# This script takes in a URL as an argument, sends a GET request to the URL
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "$1"
