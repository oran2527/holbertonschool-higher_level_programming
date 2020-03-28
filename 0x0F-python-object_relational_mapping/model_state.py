#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
'''Type importation'''
from sqlalchemy.ext.declarative import declarative_base
'''Base class'''

Base = declarative_base()


class State(Base):
    '''State Class'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
