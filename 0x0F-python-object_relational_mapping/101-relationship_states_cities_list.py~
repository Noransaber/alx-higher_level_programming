#!/usr/bin/python3
"""
t lists all State objects, and corresponding
City objects, contained in the database
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id, City.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for c in states.cities:
            print("\t{}: {}".format(c.id, c.name))

    session.close()
