#!/usr/bin/python3
"""This defines our state class."""
from models.base_model import BaseModel


class State(BaseModel):
    """This is representing a state.

    Attributes:
        name (str): The name of our state.
    """

    name = ""
