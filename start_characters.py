
from character import *

class start_characters:

    def return_player():
        # hp, defense, sprite, x, y, player
        return character(100, 10, '@', 0, 0, player = True)
