#!/usr/bin/python3
"""User test"""
from datetime import datetime
import inspect
import models
import pep8 as pycodestyle
from models.base_model import BaseModel
import time
import unittest
from unittest import mock
Model = models.state.State
module_doc = models.state.__doc__
path1 = "models/state.py"
path2 = "tests/test_models/test_state.py"


class DocsTest(unittest.TestCase):
    """Test to check behaviors"""

    @classmethod
    def setUpClass(self):
        """setting up tests"""
        self.self_funcs = inspect.getmembers(Model, inspect.isfunction)

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
                         "state.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "test_state.py needs a docstring")

        """Test classes doctring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "State class needs a docstring")

    def test_func_docstrings(self):
        """test func dostrings"""
        for func in self.self_funcs:
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
