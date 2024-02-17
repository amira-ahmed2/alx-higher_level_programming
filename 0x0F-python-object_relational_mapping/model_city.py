#!/usr/bin/python3
"""
This contains the class definition of a city
and an instance Base = declarative_base():
"""

from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class City(Base):
    """State City

    Attributes:
        __tablename__ (str): The City name
        id (int): The City id
        name (str): The City name
        state_id: the id state class

    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
