#!/usr/bin/python3
"""__init__ The magic method of our models file directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
