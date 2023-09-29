#!/usr/bin/python3
"""
takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""

import requests
from sys import argv
import json

if __name__ == "__main__":
    d = {"q": argv[1] if len(argv) > 1 else ""}
    try:
        request = requests.post("http://0.0.0.0:5000/search_user", data=d)
        request.raise_for_status()

        try:
            jd = request.json()
            if jd:
                print("[{}] {}".format(jd.get("id"), jd.get("name")))
            else:
                print("No result")
        except json.JSONDecodeError:
            print("Invalid JSON response")
    except requests.RequestException as e:
        print(f"Request error: {e}")
