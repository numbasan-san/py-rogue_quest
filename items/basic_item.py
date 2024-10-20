
from colorama import *

class basic_item:

    def __init__(self, name, sprite, x, y, func = None, to_player = False):
        self.name = name
        self.sprite = sprite
        self.x = x
        self.y = y
        self.color = Fore.CYAN
        self.func = func
        self.to_player = to_player
