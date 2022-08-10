#!/usr/bin/python3
"""State Class implementation"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Representation of a State"""

    __tablename__ = 'states'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(128), nullable=False)
