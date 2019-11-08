#!/usr/bin/python3
"""Console AirBnB"""

import cmd
class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "
    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file"""
        return True

    def create(self, *args):
        """Creates an instance"""
         if not args[0]:
            print("** class name missing **")
            return
        

    def show(self):

    def destroy(self):

    def all(self):

    def update(self):


if __name__ == '__main__':
    HBNBCommand().cmdloop()
