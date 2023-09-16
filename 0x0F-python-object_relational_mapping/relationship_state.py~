#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
"""
    creates a States class based on Base class.
"""

Base = declarative_base()


class State(Base):
    """
        Oure state class.
        Attribute: table name
        id: integer, unique key
        name: String
        cities: Relationship with the other table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        cascade="all, delete-orphan",
        backref=backref("state", cascade="all"),
        single_parent=True)
