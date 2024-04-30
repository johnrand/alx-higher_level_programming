#!/bin/bash
#--++Displayes the body of the size of response to curl's request in bytes
curl -s "{$1}" | wc -c
