#!/usr/bin/python3
""" Write a script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).all()
    Louisiana = State(name="Louisiana")
    session.add(Louisiana)
    session.commit()
    print(Louisiana)

    session.close()
