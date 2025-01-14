#!/usr/bin/python3
"""
City module
"""

from models.base_model import BaseModel, Base
from models.state import State
from os import environ
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """ City class :City class to represent a city
    City class :City class to represent a city"""

    if (storage_engine == "db"):
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey(State.id))
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        name = ""
        state_id = ""
