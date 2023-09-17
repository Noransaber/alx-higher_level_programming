#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
"""
from sys import ar
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import query

if __name__ == "__main__":
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(url.format(ar[1], ar[2], ar[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
