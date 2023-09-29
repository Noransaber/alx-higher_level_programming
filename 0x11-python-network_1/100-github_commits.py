#!/usr/bin/python3
""" evaluates candidates applying for a back-end
position with multiple technical challenges,
like this one:"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10"\
          .format(argv[2], argv[1])

    req = requests.get(url)
    cmts = req.json()
    for cmt in cmts:
        print("{}: {}".format(cmt.get("sha"),
                              cmt.get("commit").get("author").get("name")))
