#!/usr/bin/python3
"""Provides a script to retrieve and display all states using MySQLdb.
Database: hbtn_0e_0_usa
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         password=argv[2], database=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
