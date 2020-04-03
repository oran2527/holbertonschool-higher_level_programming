#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
'''Type importation'''
from sqlalchemy.ext.declarative import declarative_base
'''Base class'''
from sqlalchemy.orm import relationship
''' relationship '''
from relationship_city import Base, City
''' City class '''


class State(Base):
    '''State Class'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all, delete-orphan",
        backref="state",
    )
