#!/usr/bin/python3
"""This module displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

from sys import argv as av
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=av[1],
                         passwd=av[2], db=av[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name LIKE '{:s}'\
                ORDER BY id ASC".format(av[4]))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == av[4]:
            print(f"{row}")
    cur.close()
    db.close()
