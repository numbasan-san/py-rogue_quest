
from colorama import *

class basic_environment_item:

    def __init__(self, name, sprite, x, y, func = None):
        self.name = name
        self.sprite = sprite
        self.x = x
        self.y = y
        self.color = Fore.LIGHTCYAN_EX
        self.func = func
