#!/usr/bin/python3
""" Write a script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    Louisiana = State(name="Louisiana")
    session.add(Louisiana)
    session.commit()
    print(Louisiana.id)
    session.close()
