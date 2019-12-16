#!/usr/bin/python3
# This script lists all states with a name starting with N (upper N) from the
# database hbtn_0e_0_usa

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    database = MySQLdb.Connect(user=username,
                               passwd=password,
                               db=database_name,
                               port=3306)
    cur = database.cursor()
    cur.execute("SELECT * FROM states WHERE " +
                "name LIKE BINARY 'N%' ORDER BY 'states.id' ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    database.close()
