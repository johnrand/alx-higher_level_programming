#!/usr/bin/python3

"""Module that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    token = HTTPBasicAuth(username, password)
    request = requests.get('https://api.github.com/user', auth=token)
    print(request.json().get('id'))
