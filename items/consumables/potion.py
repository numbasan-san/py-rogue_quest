
from items.basic_item import basic_item
from utilities import *

class potion:

    # name, sprite, x, y, func, to_player
    def start(self, x = 1, y = 1):
        name = 'Poción'
        sprite = '+'
        to_player = True
        return basic_item('pt-+', name, sprite, x, y, self.use_function, to_player = to_player)

    def use_function(self, player):
        if player.hp < player.max_hp:
            hp_txt = '10' if (player.hp + 10) < player.max_hp else (player.max_hp - player.hp)
            player.hp = (player.hp + 10) if (player.hp + 10) < player.max_hp else player.max_hp
            utilities.print_effect(f'\nSalud recuperada en [{hp_txt}].')
            return True
        else:
            utilities.print_effect('\nNo se puede usar la poción. Vida del jugador al máximo.')
            return False
