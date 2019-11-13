#!/usr/bin/python3
"""test for user"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """test the User class"""

    def setUp(self):
        """Sets up test methods."""
        FileStorage._FileStorage__file_path = "test_json"
        self.user = User()
        self.user.first_name = "Betty"
        self.user.last_name = "Holberton"
        self.user.email = "airbnb@holbertonshool.com"
        self.user.password = "root"
        self.user.save()

    def test_docstring_User(self):
        """checking for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes_User(self):
        """chekcing if User have attributes"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_is_subclass_User(self):
        """test if User is subclass of Basemodel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attribute_types_User(self):
        """test attribute type for User"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_save_User(self):
        """test if the save works"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_User(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.user), True)

    def tearDown(self):
        os.remove(FileStorage._FileStorage__file_path)


if __name__ == "__main__":
    unittest.main()
