#!/usr/bin/python3
"""Print all City objects from the database
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for row in session.query(State, City).filter(State.id == City.state_id):
        print("{}: ({}) {}".format(
              row.State.name, row.City.id, row.City.name))

    session.commit()
    session.close()
