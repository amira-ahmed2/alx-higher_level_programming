#!/usr/bin/python3
"""
This deletes all State objects with
a name containing the letter a from
the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database.
    """

    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()

    for inst in session.query(State).filter(State.name.contains('a')):
        session.delete(inst)

    session.commit()
    session.close()
