
from items.basic_item import basic_item
from utilities import *

class potion_power:

    # name, sprite, x, y
    def start(self, x = 1, y = 1):
        name = 'Poción de Poder'
        sprite = 'x'
        to_player = True
        return basic_item(name, sprite, x, y, self.use_function, to_player = to_player)

    def use_function(self, player):
        player.damage += 10
        player.base_damage += 10
        utilities.print_effect('\nAtaque del jugador aumentado.\n')
        return True
