#!/usr/bin/python3
"""
This that prints all City objects from
the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
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

    for c, s in session.query(City, State).join(State).all():
        print("{}: ({:d}) {}".format(s.name, c.id, c.name))

    session.commit()
    session.close()
