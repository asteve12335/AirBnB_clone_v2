#!/usr/bin/python3
"""
    Amenity module
"""
from models.base_model import BaseModel, Base
from models.place import place_amenity
from os import environ
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """
        Amenity class
    """

    if (storage_engine == "db"):
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place",
            secondary=place_amenity, back_populates="amenities")
    else:
        name = ""
