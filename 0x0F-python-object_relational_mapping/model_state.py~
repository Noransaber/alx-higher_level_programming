#!/usr/bin/python3
"""First state model"""
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine()
Base = declarative_base()


class State(Base):
    """State class inhrit from BASE"""

    __tablename__ = "state"
    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
