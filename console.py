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
            data = args.split()
            if data[0] != "BaseModel" and data[0] != "User" and data[0] != "State" and \
               data[0] != "City" and data[0] != "Amenity" and data[0] != "Place" and \
               data[0] != "Review":
                print("* class doesn't exist **")
            else:
                obj = eval("{}()".format(data[0]))
                obj.save()
                print(obj.id)

    def do_show(self, args):
        '''Print the object with id specified and his dictionary'''
        if not args:
            print('** class name missing **')
        else:
            s = ""
            for i in args:
                s += i
            data = s.split()
            if data[0] != "BaseModel" and data[0] != "User" and data[0] != "State" and \
               data[0] != "City" and data[0] != "Amenity" and data[0] != "Place" and \
               data[0] != "Review":
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                if len(data) < 2:
                    print("** instance id missing **")
                else:
                    if (str(data[0]) + "." + str(data[1])) in all_objs:
                        print(storage.all()[str(data[0]) + "." + str(data[1])])
                    else:
                        print("** no instance found **")

    def do_destroy(self, args):
        if not args:
            print('** class name missing **')
        else:
            s = ""
            for i in args:
                s += i
            data = s.split()
            if data[0] != "BaseModel" and data[0] != "User" and data[0] != "State" and \
               data[0] != "City" and data[0] != "Amenity" and data[0] != "Place" and \
               data[0] != "Review":
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                if len(data) < 2:
                    print("** instance id missing **")
                else:
                    if ( + "." + str(data[1])) in all_objs:
                        del storage.all()[str(data[0]) + "." + str(data[1])]
                        storage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, args):
        if args:
            s = ""
            for i in args:
                s += i
            data = s.split()
            if data[0] != "BaseModel" and data[0] != "User" and data[0] != "State" and \
               data[0] != "City" and data[0] != "Amenity" and data[0] != "Place" and \
               data[0] != "Review":
                print("** class doesn't exist **")
                return
        all_objs = storage.all()
        all_objs = [str(j) for j in all_objs.values()]
        print(all_objs)

    def do_update(self, args):
        if not args:
            print('** class name missing **')
        else:
            s = ""
            for i in args:
                s += i
            data = s.split()
            if data[0] != "BaseModel" and data[0] != "User" and data[0] != "State" and \
               data[0] != "City" and data[0] != "Amenity" and data[0] != "Place" and \
               data[0] != "Review":
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                if len(data) < 2:
                    print("** instance id missing **")
                else:
                    if (str(data[0]) + "." + str(data[1])) in all_objs:
                        if len(data) < 3:
                            print("** attribute name missing **")
                        else:
                            if len(data) < 4:
                                print("** value missing **")
                            else:
                                setattr(storage.all()[str(data[0]) +
                                        "." + str(data[1])], data[2], data[3])
                    else:
                        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
