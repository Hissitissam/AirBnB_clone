#!/usr/bin/env python3
"""Module for HBNBCommand class."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Print help message for quit command."""
        print("Quit command to exit the program \n")

    def do_EOF(self, line):
        """Handle EOF (Ctrl+D) to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()