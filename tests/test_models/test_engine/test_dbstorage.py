#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import models
import inspect
import time
import json
from unittest import mock
import os
from models.engine import file_storage
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.state import State
from models.place import Place
from models.base_model import BaseModel
from models import storage
import pep8 as pycodestyle

Model = file_storage.FileStorage
FileStorage = file_storage.FileStorage
path1 = "models/engine/db_storage.py"
path2 = "tests/test_models/test_engine/test_dbstorage.py"
module_doc = models.city.__doc__

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "Review": Review,
           "City": City, "User": User, "State": State, "Place": Place}


class TestBaseModelDocs(unittest.TestCase):
    """Test to check behaviors"""

    @classmethod
    def setUpClass(self):
        """setting up tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8(self):
        """Testing pep8"""
        for path in [path1,
                     path2]:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test classes doctring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """test func dostrings"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )
