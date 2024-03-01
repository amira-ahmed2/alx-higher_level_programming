#!/usr/bin/python3
"""Write a Python script that takes in
a letter and sends a POST request to
http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data={"q": letter})
    try:
        resp = req.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
