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


class BaseModelTest(unittest.TestCase):
    """ Test for BaseModel Class """

    def setUp(self):
        FileStorage._FileStorage__file_path = "test_json"
        self.my_model = BaseModel()
        self.my_model.name = "Holberton"
        self.my_model.my_number = 89
        self.my_model2 = BaseModel()
        self.my_model2.name = "Holberton"
        self.my_model2.my_number = 89
        self.my_model.save()
        self.my_model2.save()
        self.dic = self.my_model.to_dict()
        self.my_new_model = BaseModel(**self.dic)
        self.all_objs = storage.all()

    def test_base_01(self):
        """ test of the task 03 """

        self.assertEqual(str(type(self.my_model)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertEqual(self.my_model.name, "Holberton")
        self.assertEqual(self.my_model.my_number, 89)
        self.assertEqual(self.my_model.name, "Holberton")
        self.assertEqual(self.my_model.my_number, 89)
        self.assertEqual(self.dic['name'], "Holberton")
        self.assertEqual(self.dic['my_number'], 89)
        self.assertEqual(self.dic["created_at"],
                         self.my_model.created_at.isoformat())
        self.assertEqual(self.dic["updated_at"],
                         self.my_model.updated_at.isoformat())
        self.assertEqual(type(self.dic['created_at']), str)
        self.assertEqual(type(self.dic['updated_at']), str)
        self.assertEqual(str(type(self.dic)), "<class 'dict'>")
        self.assertEqual(str(self.dic["__class__"]), "BaseModel")
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertTrue(issubclass(type(self.my_model), BaseModel))
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertNotEqual(self.my_model.id, self.my_model2.id)
        self.assertNotEqual(self.my_model.created_at,
                            self.my_model2.created_at)
        self.assertNotEqual(self.my_model.updated_at,
                            self.my_model2.updated_at)

    def test_base_02(self):
        """ test of the task 04 """
        self.assertEqual(self.my_model.id, self.my_new_model.id)
        self.assertEqual(self.my_model.updated_at,
                         self.my_new_model.updated_at)
        self.assertEqual(self.my_model.created_at,
                         self.my_new_model.created_at)
        self.assertEqual(self.my_model.name, "Holberton")
        self.assertEqual(self.my_model.my_number, 89)
        self.assertEqual(self.my_model.name, self.my_new_model.name)
        self.assertEqual(self.my_model.my_number, self.my_new_model.my_number)
        self.assertEqual(self.my_model.__class__, self.my_new_model.__class__)
        self.assertNotEqual(self.my_model, self.my_new_model)

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
        self.assertEqual(self.all_objs[self.my_model.__class__.__name__ + "." +
                                       self.my_model.id].name, "Holberton")
        self.assertEqual(self.all_objs[self.my_model.__class__.__name__ + "." +
                                       self.my_model.id].my_number, 89)
        self.assertEqual(self.all_objs[self.my_model.__class__.__name__ + "." +
                                       self.my_model.id].id, self.my_model.id)
        self.assertEqual(self.all_objs[self.my_model.__class__.__name__ + "." +
                                       self.my_model.id].created_at,
                         self.my_model.created_at)
        self.assertEqual(self.all_objs[self.my_model.__class__.__name__ + "." +
                                       self.my_model.id].updated_at,
                         self.my_model.updated_at)

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

    def tearDown(self):
        os.remove(FileStorage._FileStorage__file_path)


if __name__ == "__main__":
    unittest.main()
