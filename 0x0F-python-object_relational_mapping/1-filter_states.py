#!/usr/bin/python3
"""This module lists all 'states' from a database
through command line
"""

from sys import argv as av
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=av[1],
                         passwd=av[2], db=av[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name\
                LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(f"{row}")
    cur.close()
    db.close()
