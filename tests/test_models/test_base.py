#!/usr/bin/python3
"""
Unittest for base module
"""
import io
import os
import unittest
import unittest.mock
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_Base(unittest.TestCase):
    """ Test for BaseModel Class """

    def setUp(self):
        pass

    def test_base_01(self):
        """ test of the task 03 """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        dic = my_model.to_dict()

        self.assertEqual(str(type(my_model)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_model.my_number, 89)
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_model.my_number, 89)
        self.assertEqual(dic['name'], "Holberton")
        self.assertEqual(dic['my_number'], 89)
        self.assertEqual(dic["created_at"], my_model.created_at.isoformat())
        self.assertEqual(dic["updated_at"], my_model.updated_at.isoformat())
        self.assertEqual(str(type(dic)), "<class 'dict'>")
        self.assertEqual(str(dic["__class__"]), "BaseModel")
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(issubclass(type(my_model), BaseModel))

    def test_base_02(self):
        """ test of the task 04 """
        FileStorage._FileStorage__file_path = "test_json"
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)

        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_model.my_number, 89)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)
        self.assertEqual(my_model.__class__, my_new_model.__class__)
        self.assertNotEqual(my_model, my_new_model)

    def test_base_03(self):
        """ test of the task 04 """
        dic = {"__class__": "BaseModel",
               "updated_at": datetime.now().isoformat(),
               "created_at": datetime.now().isoformat(),
               "id": uuid.uuid4(),
               "name": "Holberton",
               "city": "Bogota",
               "int": 99,
               "float": 9.9999}
        my_model = BaseModel(**dic)
        self.assertEqual(my_model.to_dict(), dic)

    def test_base_04(self):
        """ test of the task 05 """
        FileStorage._FileStorage__file_path = "test.json"
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        all_objs = storage.all()
        self.assertEqual(all_objs[my_model.__class__.__name__ + "." +
                                  my_model.id].name, "Holberton")
        self.assertEqual(all_objs[my_model.__class__.__name__ + "." +
                                  my_model.id].my_number, 89)
        self.assertEqual(all_objs[my_model.__class__.__name__ + "." +
                                  my_model.id].id, my_model.id)
        self.assertEqual(all_objs[my_model.__class__.__name__ + "." +
                                  my_model.id].created_at, my_model.created_at)
        self.assertEqual(all_objs[my_model.__class__.__name__ + "." +
                                  my_model.id].updated_at, my_model.updated_at)
        os.remove(FileStorage._FileStorage__file_path)

    def test_base_errors_01(self):
        with self.assertRaises(Exception) as e:
            BaseModel.to_dict()
        s = "to_dict() missing 1 required positional argument: 'self'"
        self.assertTrue(s in str(e.exception))

    def test_base_errors_02(self):
        with self.assertRaises(Exception) as e:
            my_model = BaseModel()
            my_model.save(32123213)

        s = "save() takes 1 positional argument but 2 were given"
        self.assertTrue(s in str(e.exception))

    def test_base_errors_03(self):
        with self.assertRaises(Exception) as e:
            my_model = BaseModel()
            my_model.to_dict(32123213)

        s = "to_dict() takes 1 positional argument but 2 were given"
        self.assertTrue(s in str(e.exception))

    def test_base_errors_04(self):
        with self.assertRaises(Exception) as e:
            my_model = BaseModel()
            my_model.__str__(32123213)

        s = "__str__() takes 1 positional argument but 2 were given"
        self.assertTrue(s in str(e.exception))

    def test_base_errors_05(self):
        with self.assertRaises(Exception) as e:
            my_model = BaseModel()
            my_model.blabla(32123213)

        s = "'BaseModel' object has no attribute 'blabla'"
        self.assertTrue(s in str(e.exception))


if __name__ == "__main__":
    unittest.main()
