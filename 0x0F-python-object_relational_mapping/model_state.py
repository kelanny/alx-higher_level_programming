#!/usr/bin/python3
"""python file that contains the class definition of a State
And an instance Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    
    def __str__(self):
        """Return the object in string format"""
        return "{}: {}".format(self.id, self.name)
    
    def __repr__(self):
        """Return the object in string format"""
        return "{}: {}".format(self.id, self.name)

