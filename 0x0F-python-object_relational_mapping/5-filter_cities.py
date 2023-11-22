#!/usr/bin/python3
"""List all cities from MySQLdb.
Database: hbtn_0e_0_usa
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         password=argv[2], database=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name, cities.name, states.name FROM cities
            INNER JOIN states ON states.id=cities.state_id
            WHERE states.name=%s""", (argv[4], ))
    rows = cur.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=", ")
    cur.close()
    db.close()
