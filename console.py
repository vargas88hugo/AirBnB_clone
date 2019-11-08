#!/usr/bin/python3
"""Console AirBnB"""

import cmd
from models.base_model import BaseModel
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
        if args == "" or args is None:
            print("** class name missing **")
        elif args not in storage.classes():
            print ("** class doesn't exist **")

#    def do_show(self, args):
        
#    def do_destroy(self, args):

#    def do_all(self, args):

#    def do_update(self, args):


if __name__ == '__main__':
    HBNBCommand().cmdloop()
