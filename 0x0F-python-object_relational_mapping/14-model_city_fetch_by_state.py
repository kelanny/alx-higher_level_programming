#!/usr/bin/python3
""" deletes all State objects with a name containing the letter a
database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State)\
        .filter(City.state_id == State.id).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(city.state_name, city.id, city.name))

    session.close()
