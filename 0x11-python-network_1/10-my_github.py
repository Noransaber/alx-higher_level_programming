#!/usr/bin/python3
"""
 takes your GitHub credentials
 (username and password) and uses the
 GitHub API to display your id
 """


import requests
from sys import argv

if __name__ == "__main__":
    a = (argv[1], argv[2])
    request = requests.get("https://api.github.com/user", auth=a)
    print(request.json().get("id"))
