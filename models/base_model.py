#!/usr/bin/python3
"""Module Base class for the AirBnB console"""

import uuid
from datetime import datetime

format = '%Y-%m-%dT%H:%M:%S.%f'

class BaseModel:
    """class defines all common attributes/methods"""

    def __init__(self, *args, **kwargs):
        '''inicialization Base
        *args won’t be used
        if kwargs is not empty:
        each key of this dictionary is an attribute name
        each value of this dictionary is the value of this attribute name
        '''
        if kwargs:
            for key, value in kwargs.items():
                if x == 'created_at' or x == 'updated_at':
                    value = datetime.strptime(value, format)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''human readable'''
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        '''updates the public instance attribute
        updated_at with the current datetime'''
        self.update_at = datetime.now()


    def to_dict(self):
         '''creates dictionary of the class  and returns
            a dictionary of all the key values in __dict__'''
         dic2 = self.__dict__.copy()

         return dic2
