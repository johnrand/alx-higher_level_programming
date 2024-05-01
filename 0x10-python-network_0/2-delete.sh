#!/bin/bash
#++sends a DELETE req to URL passed as 1st arg & displays body of response
curl -s "$1" -X DELETE
