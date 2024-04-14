#!/usr/bin/python3
"""lists all State objects that contain the letter a
Database: hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    a_states = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id).all()
    for state in a_states:
        print("{}: {}".format(state.id, state.name))
    session.close()
