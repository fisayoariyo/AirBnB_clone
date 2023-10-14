#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """This represents our city.

    Attributes:
        state_id (str): This is our state id.
        name (str): The reps the name of the city.
    """

    state_id = ""
    name = ""
