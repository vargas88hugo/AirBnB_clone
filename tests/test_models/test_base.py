#!/usr/bin/python3
"""
Unittest for base module
"""
import io
import unittest
import unittest.mock
from models.base_model import BaseModel


class Test_Base(unittest.TestCase):
    """ Test for BaseModel Class """

    def setUp(self):
        pass

    def test_base_01(self):
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        dic = my_model.to_dict()

        self.assertEqual(str(type(my_model)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_model.my_number, 89)
        self.assertEqual(dic['name'], "Holberton")
        self.assertEqual(dic['my_number'], 89)
        self.assertEqual(str(type(dic)), "<class 'dict'>")
        self.assertEqual(str(dic["__class__"]), "BaseModel")

    def test_base_02(self):
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)

        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)
        self.assertEqual(my_model.__class__, my_new_model.__class__)
        self.assertNotEqual(my_model, my_new_model)
