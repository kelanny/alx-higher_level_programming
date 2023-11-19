#!/usr/bin/python3
"""retrieve and display list of states filtered by user's input using MySQLdb.
Database: hbtn_0e_0_usa
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         password=argv[2], database=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
