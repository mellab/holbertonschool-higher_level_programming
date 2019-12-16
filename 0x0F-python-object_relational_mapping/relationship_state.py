#!/usr/bin/python3
# Relationship state


from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                unique=True
                nullable=False,
                )
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete-orphan")
