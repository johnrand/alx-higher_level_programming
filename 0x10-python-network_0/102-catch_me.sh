#!/bin/bash
# makes req to 0.0.0.0:5000/catch_me that causes server to res with messg containing You got me!, in body of res
curl -sLX PUT -H "origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
