
from colorama import *

class BasicEnvironmentItem:

    def __init__(self, name, sprite, x, y, code, func = None):
        self.name = name
        self.sprite = sprite
        self.x = x
        self.y = y
        self.color = Fore.LIGHTCYAN_EX
        self.func = func
        self.code = code
