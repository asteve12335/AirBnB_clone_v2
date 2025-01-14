#!/usr/bin/python3
"""
    Place module
"""
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
import models

storage_engine = environ.get("HBNB_TYPE_STORAGE")

if storage_engine == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """
        Place class to represent places
        Place class to represent places
    """
    __tablename__ = "places"
    if (storage_engine == "db"):
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship("Review", back_populates="place")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 back_populates="place_amenities",
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """getter function for reviews attribute"""
            result = []
            temp = models.dummy_classes['Review']
            for r in models.storage.all(temp).values():
                if r.place_id == self.id:
                    result.append(r)
            return result

        @property
        def amenities(self):
            """getter function for amenity attribute"""
            result = []
            temp = models.dummy_classes['Amenity']
            for m in models.storage.all(temp).values():
                if m in self.amenity_ids:
                    result.append(m)
            return result

        @amenities.setter
        def amenities(self, obj):
            """ setter for amenities class """
            tmp = models.dummy_classes['Amenity']
            if (isinstance(obj, models.storage.all(tmp))):
                self.amenity_ids.append(obj.id)
