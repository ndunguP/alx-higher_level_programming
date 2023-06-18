#!/usr/bin/python3
"""Print the state object with the name passed as the argument from the
database
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3],
                           sys.argv[4]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    flag = 0
    for state in session.query(State).all():
        if state.name == sys.argv[4]:
            flag = 1
            print("{}".format(state.id))
    if flag == 0:
        print("Not found")
    session.close()
