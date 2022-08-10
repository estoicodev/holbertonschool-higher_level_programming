#!/usr/bin/python3
"""This module lists all cities of that state,
using the database hbtn_0e_4_usa"""

from sys import argv as av
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=av[1],
                         passwd=av[2], db=av[3])
    cur = db.cursor()
    cur.execute("SELECT c.name\
                FROM cities c\
                INNER JOIN states s\
                ON s.id=c.state_id\
                WHERE s.name=%(search)s\
                ORDER BY c.id", {'search': av[4]})
    rows = cur.fetchall()

    output = ""
    for i in range(len(rows)):
        output += rows[i][0]
        if i < len(rows) - 1:
            output += ', '
    print(output)
    cur.close()
    db.close()
