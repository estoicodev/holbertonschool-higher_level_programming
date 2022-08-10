#!/usr/bin/python3
"""This module lists all cities from the database hbtn_0e_4_usa"""

from sys import argv as av
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=av[1],
                         passwd=av[2], db=av[3])
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name\
                FROM cities c\
                JOIN states s\
                ON s.id=c.state_id\
                ORDER BY c.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(f"{row}")
    cur.close()
    db.close()
