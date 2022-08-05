#!/usr/bin/python3
"""This module displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
from sys import argv as av
import MySQLdb

db = MySQLdb.connect(host="localhost", user=av[1], passwd=av[2], db=av[3])
cur = db.cursor()
cur.execute("SELECT * FROM hbtn_0e_0_usa.states\
            WHERE states.name = %(search)s\
            ORDER BY states.id", {'search': av[4]})
rows = cur.fetchall()
for row in rows:
    print(f"{row}")
