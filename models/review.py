#!/usr/bin/python3
"""This is to define our Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is representing a review from clients.

    Attributes:
        place_id (str): Our Place id.
        user_id (str): OR client/User id.
        text (str): Representing the text/commen.
    """

    place_id = ""
    user_id = ""
    text = ""
