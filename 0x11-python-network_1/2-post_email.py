#!/usr/bin/python3
"""
 takes in a URL and an email, sends a POST
 request to the passed URL with the email as a
 parameter, and displays the body of the response
 (decoded in utf-8)
 """

from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    d = parse.urlencode({"email": argv[2]}).encode('utf-8')
    with request.urlopen(argv[1], d) as p:
        print(p.read().decode('utf-8'))
