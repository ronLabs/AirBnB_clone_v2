#!/usr/bin/python3
import unittest
import os.path
import os
import models
from datetime import datetime
from models.engine.db_storage import DBStorage
from models import *
from console import HBNBCommand

@unittest.skipIf(models.is_db != 'db', 'Not testing Dbstorage')
class Test_dbstorage(unittest.TestCase):
    """ testing dbstorage class """
    def setUpClass(self):
        """setting up class"""
        self.HNBNcom = HBNBCommand
        self.Db = DBStorage

        arg_list = {'updated_at': datetime(2021, 10, 8, 13, 31, 53, 331997),
                     'id': 'c519fb40-3f5c-448b-945c-2ce8eaaf4931',
                     'created_at': datetime(2021, 10, 8, 13, 31, 53, 331997),
                     'name': 'holbie'}
        self.model = City(arg_list)

    def test_init(self):
        """testing init"""
        self.assertNotEqual(self.Db._DBStorage__engine, None)
        self.assertEqual(self.Db._DBStorage__session, None)

    def test_all_method(slef):
        """testing that all method return all args"""
