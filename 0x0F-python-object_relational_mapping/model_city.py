#!/usr/bin/python3
"""
Python file that contains the class definition of a City
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    State class that inherits from Base
    """
    __tablename__ = "city"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey=('states.id') nullable=False)
