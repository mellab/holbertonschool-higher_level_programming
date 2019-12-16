#!/usr/bin/python3
# Relationship city


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer,
                unique=True,
                primary_key=True,
                autoincrement="auto",
                nullable=False)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
