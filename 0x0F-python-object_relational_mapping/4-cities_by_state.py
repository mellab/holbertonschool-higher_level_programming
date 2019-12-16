#!/usr/bin/python3
# This script lists all cities from the database hbtn_0e_4_usa

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
    query = "SELECT cities.id, cities.name, states.name FROM cities " +\
            "JOIN states ON cities.state_id = states.id ORDER BY id ASC;"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    database.close()
