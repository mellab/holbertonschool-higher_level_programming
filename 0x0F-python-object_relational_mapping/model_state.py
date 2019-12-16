#!/usr/bin/python3
# This script takes in the name of a state as an argument and lists all cities
# of that state, using the database hbtn_0e_4_usa

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)
