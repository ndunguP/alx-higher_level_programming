#!/usr/bin/python3
"""List all State object that contain the letter a from the database
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        flag = 0
        for i in state.name:
            if i == 'a':
                flag = 1
        if flag == 1:
            print("{}: {}".format(state.id, state.name))
    session.close()
