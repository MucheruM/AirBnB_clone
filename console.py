#!/usr/bin/python3
"""Console Module to intertract with the AirBnB Project"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB Command Terminal Class"""

    prompt = "(hbnb) "

    def do_quit(self, argument):
        """Defines quit option"""
        return True

    def emptyline(self):
        """Defines Empty option"""
        pass

    def do_EOF(self, argument):
        """Defines EOF option"""
        print()
        return True

if __name__ == "__main__":
    """Infinite loop"""
    HBNBCommand().cmdloop()
