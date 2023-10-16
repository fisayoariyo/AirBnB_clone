#!/usr/bin/python3
"""We define our Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Shows an amenity.

    Attributes include:
        name (str): Represents the name of the amenity.
    """

    name = ""
