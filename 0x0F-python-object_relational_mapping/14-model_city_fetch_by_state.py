#!/usr/bin/python3
# This script prints all City objects from the database hbtn_0e_14_usa


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City


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

    for c, s in session.query(City, State).filter(City.state_id == State.id):
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
