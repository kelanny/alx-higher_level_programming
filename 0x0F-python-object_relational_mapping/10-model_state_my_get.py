#!/usr/bin/python3
"""e letter a
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
    search_state = session.query(State).filter_by(name=argv[4]).first()
    if search_state:
        print(search_state.id)
    else:
        print('Not found')
    session.close()
