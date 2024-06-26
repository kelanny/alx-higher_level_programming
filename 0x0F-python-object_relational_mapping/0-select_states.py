#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         password=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
