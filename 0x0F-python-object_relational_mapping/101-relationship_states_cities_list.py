#!/usr/bin/python3
# This script lists all State objects, and corresponding City objects,
# contained in the database hbtn_0e_101_usa


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
    states_list = session.query(State).order_by(State.id)
    for state in states_list:
        print("{:d}: {:s}".format(state.id, state.name))
        for cities in state.cities:
            print("    {:d}: {:s}".format(cities.id, cities.name))
    session.close()
