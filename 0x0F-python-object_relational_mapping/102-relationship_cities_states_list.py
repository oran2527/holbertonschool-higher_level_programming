#!/usr/bin/python3
'''Task 17 select all cities with its state'''
from model_state import Base, State
from model_city import City
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
    a = State.name
    b = State.id
    c = City.id
    d = City.name
    e = City.state_id
    rs = ses.query(a, b, c, d).filter(b == e).order_by(c)
    for w in rs:
        s = str(w[0])
        st_name = str(s.replace(",", "").replace("(", "").replace(")\
", "").replace("'", ""))
        s = str(w[1])
        st_id = str(s.replace(",", "").replace("(", "").replace(")\
", "").replace("'", ""))
        s = str(w[2])
        c_id = str(s.replace(",", "").replace("(", "").replace(")\
", "").replace("'", ""))
        s = str(w[3])
        c_name = str(s.replace(",", "").replace("(", "").replace(")\
", "").replace("'", ""))
        print("{}: {} -> {}".format(c_id, c_name, st_name))
