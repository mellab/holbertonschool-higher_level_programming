#!/usr/bin/python3
# This script creates the State “California” with the City “San Francisco” from
# the database hbtn_0e_100_usa: (100-relationship_states_cities.py)


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
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

    california = State(name="California")
    sanfrancisco = City(name="San Francisco")
    california.cities.append(sanfrancisco)
    session.add(california)
    session.commit()
    session.close()
