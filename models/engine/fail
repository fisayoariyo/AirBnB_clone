#!/usr/bin/python3
"""This will Define our  FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This shows our abstracted storage engine.

    Attributes:
        __file_path (str): Represents the name of the file objects are saved to.
        __objects (dict): This is a dictionary of our instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This is to return our dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """ Input in our __objects obj with the key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """This will arrange serially our __objects to JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """This is to de-serialize our JSON file __file_path to __objects, if existing."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            raise FileNotFoundError("File not found: {}".format(FileStorage.__file_path))

