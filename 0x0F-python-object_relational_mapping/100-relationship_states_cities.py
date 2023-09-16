#!/usr/bin/python3
"""reates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa"""
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    new_state = State(name="California")
    new_city = Citr(name="San Francisco")
    new_state.append(new_city)
    session.add_all([new_state, new_city)]
    session.commit()
    session.close()
