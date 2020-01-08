#!/bin/bash
# This script takes in a URL, sends a request to that URL
curl -sLI "$1" -o /dev/null -w '%{http_code}'
