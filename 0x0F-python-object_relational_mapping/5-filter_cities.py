#!/usr/bin/python3
# This script takes in the name of a state as an argument and lists all cities
# of that state, using the database hbtn_0e_4_usa

import MySQLdb
import sys

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
    query = "SELECT cities.name FROM cities " +\
            "JOIN states ON cities.state_id = states.id " +\
            "WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, (state,))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    database.close()
