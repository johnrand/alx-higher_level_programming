#!/bin/bash
# sends POST request with post parameters to passed URL, and displays body of response
curl -sL "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
