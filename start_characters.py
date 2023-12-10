
from character import *

class start_characters:

    def return_player(x, y):
        # hp, defense, sprite, x, y, player
        return character(100, 10, '@', x, y, player = True)
    
    def return_enemy():
        return character(100, 10, 'E', 2, 2)
