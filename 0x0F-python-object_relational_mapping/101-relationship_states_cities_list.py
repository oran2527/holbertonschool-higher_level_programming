#!/usr/bin/python3
'''Task 14 select all cities with its state'''
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
    rs = ses.query(b, c, d).filter(b == e).order_by(b).order_by(c)
    st = ses.query(b, a).all()
    for w in st:
        s = str(w[0])
        st_id = str(s.replace(",", "").replace("(", "").replace(")\
", "").replace("'", ""))
        s = str(w[1])
        st_name = str(s.replace(",", "").replace("(", "").replace(")\
", "").replace("'", ""))
        print("{}: {}".format(st_id, st_name))
        for q in rs:
            s = str(q[0])
            s_id = str(s.replace(",", "").replace("(", "").replace(")\
", "").replace("'", ""))
            if st_id == s_id:
                tab = "    "
                s = str(q[1])
                c_id = str(s.replace(",", "").replace("(", "").replace(")\
", "").replace("'", ""))
                s = str(q[2])
                c_name = str(s.replace(",", "").replace("(", "").replace(")\
", "").replace("'", ""))
                print("{}{}: {}".format(tab, c_id, c_name))
