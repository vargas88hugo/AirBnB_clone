#!/usr/bin/python3
"""Console AirBnB"""
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

import cmd
from models.base_model import BaseModel

xs = {'BaseModel': BaseModel, 'User': User,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "
    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Quit command to exit the program at end of file"""
        return True

    def do_create(self, args):
        """Creates an instance"""
        if not args:
            print('** class name missing **')
        else:
            arg = args.split()
            if arg[0] in xs:
                b = xs[arg[0]]()
                print(b.id)
                b.save()
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        '''Print the object with id specified and his dictionary'''
        arg = args.split()
        if not args:
            print('** class name missing **')
        else:
            if arg[0] not in xs:
                print("** class doesn't exist **")
            if len(arg) < 2:
                print("** instance id missing **")
            objects = models.storage.all()
            key = arg[0] + '.' + arg[1]
            if key not in objects:
                print("** no instance found **")
            else:
                print (objects[key])

#    def do_destroy(self, args):

#    def do_all(self, args):

#    def do_update(self, args):


if __name__ == '__main__':
    HBNBCommand().cmdloop()
