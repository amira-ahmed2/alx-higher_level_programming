#!/usr/bin/python3
"""Write a Python script that takes your GitHub credentials
(username and password) and uses
the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth
if __name__ == "__main__":
    user = sys.argv[1]
    passw = sys.argv[2]
    auth = HTTPBasicAuth(user, passw)
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))
