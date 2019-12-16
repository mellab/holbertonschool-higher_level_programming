#!/usr/bin/python3
# This script takes in an argument and displays all values in the states
# table of hbtn_0e_0_usa where name matches the argument.


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
    cur.execute("SELECT * FROM states WHERE BINARY " +
                "name='{}' ".format(state) +
                "ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    database.close()
