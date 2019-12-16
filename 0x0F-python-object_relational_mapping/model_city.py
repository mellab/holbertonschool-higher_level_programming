#!/usr/bin/python3
# This file contains the class definition of a City


from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer,
                unique=True,
                primary_key=True,
                nullable=False)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
