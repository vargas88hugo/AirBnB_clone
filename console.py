#!/usr/bin/python3
"""Console AirBnB"""
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import cmd


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
            s = ""
            for i in args:
                s += i
            if s != "BaseModel":
                print("* class doesn't exist **")
            else:
                obj = BaseModel()
                obj.save()
                print(obj.id)

    def do_show(self, args):
        '''Print the object with id specified and his dictionary'''
        arg = args.split()
        if not args:
            print('** class name missing **')
        else:
            s = ""
            for i in args:
                s += i
            data = s.split()
            if data[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                if len(data) < 2:
                    print("** no instance found **")
                else:
                    for i, j in all_objs.items():
                        if i.split(".")[1] == data[1]:
                            print(j)
                            return
                    print("** no instance found **")

    def do_destroy(self, args):
        arg = args.split()
        if not args:
            print('** class name missing **')
        else:
            s = ""
            for i in args:
                s += i
            data = s.split()
            if data[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                if len(data) < 2:
                    print("** no instance found **")
                else:
                    for i, j in all_objs.items():
                        if i.split(".")[1] == data[1]:
                            del storage.all()[i]
                            storage.save()
                            return
                    print("** no instance found **")

    def do_all(self, args):
        if args:
            s = ""
            for i in args:
                s += i
            data = s.split()
            if data[0] != "BaseModel":
                print("** class doesn't exist **")
                return
        all_objs = storage.all()
        all_objs = [str(j) for j in all_objs.values()]
        print(all_objs)

    def do_update(self, args):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
