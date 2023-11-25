#!/usr/bin/python3
""" creates the State “California” with the City “San Francisco”
database hbtn_0e_6_usa
"""


from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    california = State(name="California", cities=[City(name="San Francisco")])
    session.add(california)
    session.commit()
    session.close()
