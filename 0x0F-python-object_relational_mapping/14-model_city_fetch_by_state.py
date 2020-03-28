#!/usr/bin/python3
'''Task 14 select all cities with its state'''
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    t = 'mysql+mysqldb://{}:{}@localhost/{}'
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    s3 = sys.argv[3]
    engine = create_engine(t.format(s1, s2, s3), pool_pre_ping=True)
    session = sessionmaker()
    session.configure(bind=engine)
    ses = session()
    Base.metadata.create_all(engine)
    x = City.state_id
    records = ses.query(State.name, City.id, City.name).filter(State.id == x)
    for record in records:
        print("{}: ({}) {}".format(record[0], record[1], record[2]))
