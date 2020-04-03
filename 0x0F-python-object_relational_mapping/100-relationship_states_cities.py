#!/usr/bin/python3
'''Task 15 relationship city state'''
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy import create_engine
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
    st = State(name='California')    
    st.cities = [City(name='San Francisco')]
    ses.add(st)
    ses.commit()
