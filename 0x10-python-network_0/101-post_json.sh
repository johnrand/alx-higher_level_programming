#!/bin/bash
# send a post request with contents of a json file passed as 2nd arg to script
curl -s -H "content-type:application/json"  -d @"$2" -X POST "$1"
