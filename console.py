#!/usr/bin/python3
"""
console module
"""

import cmd
from models.base_model import BaseModel
from models.agent import Agent
from models.property import Property
from models.transaction import Transaction
from models.whishlist import Whishlist
from models.user import User
from models.property_image import Property_image
from models.message import Message, Room
from models.review import Review
from models import storage

import sys
import shlex



class ROOFMARKETCommand(cmd.Cmd):
    """Console class"""
    prompt = '(RoofMarket) ' if sys.__stdin__.isatty() else ''
    classes = {
               'BaseModel': BaseModel, 'User': User, 'Property': Property,
               'Agent': Agent, 'Transaction': Transaction, 'Whishlist': Whishlist,
               'Property_image': Property_image,
               'Message': Message, 'Review': Review, 'Room': Room
              }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_EOF(self, line):
        """Handle End-of-File (EOF) condition to exit the program gracefully"""
        print()
        return True

    def do_create(self, args):
        """ Create an object of any type

            Usage: create class_name
        """
        for i in range(1):
            arguments = shlex.split(args)
            f_arguments = arguments[1:]
            if not args:
                print("** class doesn't exist **")
                return
            elif arguments[0] not in ROOFMARKETCommand.classes:
                print("** class doesn't exist **")
                return
            new_instance = globals()[arguments[0]]()

            for my_args in f_arguments:
                key, value = my_args.split("=")
                setattr(new_instance, key, value)
            new_instance.save()
            print(new_instance.id)


    def do_destroy(self, args):
        """Delete an object or row from the database
        Usage: destroy class_name object_id
        
        """
        arguments = shlex.split(args)
        if not args:
            print("** class doesn't exist **")
            return
        elif arguments[0] not in ROOFMARKETCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(arguments) == 1:
            print("** provide the id of the object **")
            return
        ob_id = "{}.{}".format(arguments[0].lower(), arguments[1])
        for key, value in storage.all(arguments[0]).items():
            if (key == ob_id):
                value.delete()
                storage.save()

    def do_all(self, args):  
        print(storage.get_object(User))     
if __name__ == '__main__':
    ROOFMARKETCommand().cmdloop()
