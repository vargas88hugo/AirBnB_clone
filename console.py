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

    def default(self, args):
        """Method when the command is not recognized"""
        data = args.split('.')
        if len(data) >= 2:
            if data[1][:3] == "all":
                self.do_all(data[0])
            elif data[1][:5] == "count":
                self.count(data[0])
            elif data[1][:4] == "show":
                self.do_show((data))
            elif data[1][:7] == "destroy":
                self.do_destroy((data))
            elif data[1][:6] == "update":
                self.do_destroy((data))
        else:
            cmd.Cmd.default(self, args)

    def count(self, line):
        """count # of instances of a class"""
        pass

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
            if s != "BaseModel" and s != "User" and s != "State" and \
               s != "City" and s != "Amenity" and s != "Place" and \
               s != "Review":
                print("* class doesn't exist **")
            else:
                if s == "BaseModel":
                    obj = BaseModel()
                elif s == "User":
                    obj = User()
                elif s == "State":
                    obj = State()
                elif s == "City":
                    obj = City()
                elif s == "Amenity":
                    obj = Amenity()
                elif s == "Place":
                    obj = Place()
                else:
                    obj = Review()
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
            if data[0] != "BaseModel" and data[0] != "User" and\
               data[0] != "State" and data[0] != "City" and \
               data[0] != "Amenity" and data[0] != "Place" and \
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
            if data[0] != "BaseModel" and data[0] != "User" and\
               data[0] != "State" and data[0] != "City" and \
               data[0] != "Amenity" and data[0] != "Place" and \
               data[0] != "Review":
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                if len(data) < 2:
                    print("** instance id missing **")
                else:
                    if (str(data[0]) + "." + str(data[1])) in all_objs:
                        del storage.all()[str(data[0]) + "." + str(data[1])]
                        storage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, args):
        all_objs = storage.all()
        if args:
            s = ""
            for i in args:
                s += i
            data = s.split()
            if data[0] != "BaseModel" and data[0] != "User" and\
               data[0] != "State" and data[0] != "City" and \
               data[0] != "Amenity" and data[0] != "Place" and \
               data[0] != "Review":
                print("** class doesn't exist **")
                return
            a = []
            for i, j in all_objs.items():
                if data[0] in i:
                    a.append(j)
            a = [str(i) for i in a]
            print(a)
        else:
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
            if data[0] != "BaseModel" and data[0] != "User" and\
               data[0] != "State" and data[0] != "City" and \
               data[0] != "Amenity" and data[0] != "Place" and \
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
