#!/usr/bin/python3
"""States's values display"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhaost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=rgv[3],
        charset="utf8",
    )
    cur = conn.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name='{}' ORDER BY id".format(state_name)
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
