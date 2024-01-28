#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import models
import os
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quits the program."""
        return True  # Signal to exit

    def do_EOF(self, args):
        """Exits on end-of-file input."""
        print()
        return True  # Signal to exit

    def do_create(self, args):
        """Creates a new instance of a model."""
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        try:
            model_class = getattr(models, class_name)
            new_instance = model_class()
            new_instance.save()
            print(f"{new_instance.id}")
        except AttributeError:
            print(f"** class doesn't exist **")

        def do_show(self, args):
            """Shows the string representation of an instance."""
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        try:
            model_class = getattr(models, class_name)
        except AttributeError:
            print(f"** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        id = args[1]
        instance = models.storage.get(id)
        if instance:
            print(instance)
        else:
            print(f"** no instance found **")

        def do_destroy(self, args):
            """Destroys an instance based on its ID."""
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        try:
            model_class = getattr(models, class_name)
        except AttributeError:
            print(f"** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        id = args[1]
        instance = models.storage.get(id) # Call the class's get()
        if instance:
            instance.destroy() # call the instance's destroy()
            models.storage.save() # Persist changes
            print(f"** {class_name} {id} deleted**")
        else:
            print(f"** no instance found **")

        def do_all(self, args):
            """Prints all instances of a class or all instances."""
        if args:
            class_name = args[0]
        try:
            model_class = getattr(models, class_name)
            instances = models.storage.all(model_class)
        except AttributeError:
            print(f"** class doesn't exist **")
            return
        else:
            instances = models.storage.all()

        if instances:
            for instance in instances:
                print(instance)
        else:
            print("** no instances found**")

        def do_update(self, args):
            """Updates an instance's attributes with a dictionary."""
        if len(args) < 3:
            print("** usage: update <class name> <id> <dictionary representation> **")
            return

        class_name = args[0]
        try:
            model_class = getattr(models, class_name)
        except AttributeError:
            print(f"** class doesn't exist **")
            return

        id = args[1]
        instance = model_class.get(id)  # Call the class's get() method
        if instance:
            try:
                attribute_dict = eval(args[2])  # Evaluate the dictionary string
            except (SyntaxError, NameError):
                print("** invalid dictionary format **")
                return

            for attribute_name, attribute_value in attribute_dict.items():
                if hasattr(instance, attribute_name):
                    setattr(instance, attribute_name, attribute_value)
                else:
                    print(f"** attribute '{attribute_name}' does not exist **")

            models.storage.save()  # Persist changes
            print(f"** {class_name} {id} updated **")
        else:
            print(f"** no instance found **")

        def do_all(self, args):
            """Retrieves all instances of a class or all instances."""
        if args:
            class_name = args[0]
            try:
                model_class = getattr(models, class_name)
                instances = model_class.all()  # Call the class's all() method
            except AttributeError:
                print(f"** class doesn't exist **")
                return
        else:
            instances = models.storage.all()  # Retrieve all instances from storage

        if instances:
            for instance in instances:
                print(instance)
        else:
            print("** no instances found **")

        def do_count(self, args):
            """Retrieves the number of instances of a class."""
        if args:
            class_name = args[0]
            try:
                model_class = getattr(models, class_name)
                count = model_class.count()  # Call the class's count() method
                print(f"{count} {class_name} instances")
            except AttributeError:
                print(f"** class doesn't exist **")
        else:
            print("** class name missing **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()

