#!/bin/bash
# sends request to URL passed as arg & displays only status code of response.
curl -s -o /dev/null -I --w "%{http_code}" "$1"
