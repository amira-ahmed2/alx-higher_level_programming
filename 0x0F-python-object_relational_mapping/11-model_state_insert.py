#!/usr/bin/python3
"""
This adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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

    add_lou_state = State(name='Louisiana')
    session.add(add_lou_state)
    session.commit()
    print('{0}'.format(add_lou_state.id))
    session.close()
