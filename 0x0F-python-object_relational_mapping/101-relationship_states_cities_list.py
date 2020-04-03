#!/usr/bin/python3
'''Task 16 select all cities with its state'''
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
    '''a = State.name
    b = State.id
    c = City.id
    d = City.name
    e = City.state_id
    rs = ses.query(a, b, c, d).filter(b == e).order_by(b).order_by(c)
    list_st_id = []
    for w in rs:
        s = str(w[1])
        st_id = str(s.replace(",", "").replace("(", "").replace(")\
", "").replace("'", ""))
        list_st_id.append(st_id)
    new_list = sorted(list(set(list_st_id)))
    for x in new_list:
        flag = 0
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
            tab = "    "
            if x == st_id and flag == 0:
                print("{}: {}".format(st_id, st_name))
                flag = 1
            if x == st_id:
                print("{}{}: {}".format(tab, c_id, c_name))'''
    cs = ses.query(State).order_by(State.id)
    for css in cs:
        print("{}: {}".format(css.id, css.name))
        for cts in css.cities:
            print("    {}: {}".format(cts.id, cts.name))
