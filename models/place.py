#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Representing our place(bnb).

    Attributes:
        city_id (str): Our City id.
        user_id (str): Our User id.
        name (str): The name of Our place.
        description (str): Description of the our place.
        number_rooms (int): Reps the no of rooms of our place.
        number_bathrooms (int): Reps the no of our bathrooms in our place.
        max_guest (int): reps max no of guests at our place.
        price_by_night (int): reps the price by night of our place.
        latitude (float): reps the latitude of our place.
        longitude (float): reps the longitude of our place.
        amenity_ids (list): The list of all Amenity ids.
    """

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
