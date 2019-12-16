#!/usr/bin/python3
# This script lists all City objects from the database hbtn_0e_101_usa


import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(username,
                                password,
                                database_name),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    cities_list = session.query(City).order_by(City.id)
    for city in cities_list:
        print("{:d}: {:s} -> {:s}".format(city.id, city.name, city.state.name))
    session.close()
