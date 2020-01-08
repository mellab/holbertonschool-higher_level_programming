#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me
curl -sLX PUT "" -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
