#!/usr/bin/python3
"""This will define our BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This will represent our BaseModel of the Segun and FizzBnB project."""

    def __init__(self, *args, **kwargs):
        """We shall Initialize a new BaseModel.

        Arguments:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Here we update updated_at using the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """We return dictionary of our BaseModel instance.

        This will Include the key/value pair __class__ that represents 
        the class name of our object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """This will return a print/str representation of BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
