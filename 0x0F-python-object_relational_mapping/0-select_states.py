#!/usr/bin/python3
"""This module lists all 'states' from a database
through command line
"""
from sys import argv as av
import MySQLdb

db = MySQLdb.connect(host="localhost", user=av[1], passwd=av[2], db=av[3])
cur = db.cursor()
cur.execute("SELECT * from hbtn_0e_0_usa.states ORDER BY states.id")
rows = cur.fetchall()
for row in rows:
    print(f"{row}")
