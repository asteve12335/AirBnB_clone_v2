#!/usr/bin/python3
"""
    Review module
"""
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from sqlalchemy.sql.schema import ForeignKey

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class Review(BaseModel, Base):
    """
        Review class
    """
    if (storage_engine == 'db'):
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey("places.id"))
        user_id = Column(String(60), ForeignKey("users.id"))
        text = Column(String(1024), nullable=False)
        place = relationship("Place", back_populates="reviews")
    else:
        place_id = ""
        user_id = ""
        text = ""
