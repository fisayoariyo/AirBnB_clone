#!/usr/bin/python3
"""This defines our user's class."""
from models.base_model import BaseModel


class User(BaseModel):
    """This is representing a user.

    Attributes:
        email (str): reps the email of the user.
        password (str): reps the password of the user.
        last_name (str): reps the last name of the user.
        first_name (str): reps the first name of the user.
    """

    email = ""
    password = ""
    last_name = ""
    first_name = ""
