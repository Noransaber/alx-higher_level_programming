#!/usr/bin/python3
"""Listes all states"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    MyDb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
    )

    myCur = MyDb.cursor()

    myCur.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = myCur.fetchall()

    for row in rows:
        print(row)

    myCur.close()
    MyDb.close()
