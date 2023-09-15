#!/usr/bin/python3
"""displays all values in the states"""

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
    query = """
    SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query.format(argv[4])
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()