#!/usr/bin/python3
"""Provides a script to retrieve and display all states using MySQLdb.
Database: hbtn_0e_0_usa
"""

from sys import argv
import MySQLdb

host = 'localhost'
user = argv[1]
pwd = argv[2]
dbs = argv[3]

db = MySQLdb.connect(host=host, user=user, password=pwd, database=dbs)
cur = db.cursor()
cur.execute("SELECT * FROM states")
states = cur.fetchall()
for state in states:
    print(state)
