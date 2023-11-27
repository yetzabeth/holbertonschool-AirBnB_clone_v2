#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class, contains state name """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # For DBStorage
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                                cascade="all, delete-orphan")

    # For FileStorage
    if getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances
            with state_id equals to the current State.id"""
            cities_list = []
            for city_id, city in models.storage.all("City").items():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
