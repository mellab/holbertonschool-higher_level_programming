#!/usr/bin/python3
# This script takes in arguments and displays all values in the states table of
# hbtn_0e_0_usa where name matches the argument. But this time, write one that
# is safe from MySQL injections!

import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state = sys.argv[4]

    database = MySQLdb.Connect(user=username,
                               passwd=password,
                               db=database_name,
                               port=3306)
    cur = database.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC;",
                (state,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    database.close()
