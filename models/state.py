#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            cities_list = []
            all_cities = models.storage.all(City).values()
            for ct in all_cities:
                if ct.state_id == self.id:
                    cities_list.append(ct)
            return cities_list
