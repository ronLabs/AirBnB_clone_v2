#!/usr/bin/python3
"""Base model test"""
from datetime import datetime
import inspect
import models
import pep8 as pycodestyle
import time
import unittest
from unittest import mock
BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__
path1 = "models/base_model.py"
path2 = "tests/test_models/test_base_model.py"
filename = "base_model.py"


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


class TestinClassModel(unittest.TestCase):
    """Class Model Test"""
    def test_instance(self):
        """ test if the object is correctly created"""
        instance = BaseModel()
        self.assertIs(type(instance), BaseModel)
        instance.name = "Holbie"
        instance.number = 11
        types_attr = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
        }

        for attr, typ in types_attr.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, instance.__dict__)
                self.assertIs(type(instance.__dict__[attr]), typ)
        self.assertEqual(instance.name, "Holbie")
        self.assertEqual(instance.number, 11)
