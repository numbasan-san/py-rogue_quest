
from items.basic_item import basic_item
from utilities import *

class potion:

    def start(self):
        name = 'Poción'
        sprite = '+'
        to_player = True
        return basic_item(name, sprite, 1, 1, self.use_function, to_player = to_player)

    def use_function(self, player):
        if player.hp < player.max_hp:
            hp_txt = '10' if (player.hp + 10) < player.max_hp else (player.max_hp - player.hp)
            player.hp = (player.hp + 10) if (player.hp + 10) < player.max_hp else player.max_hp
            utilities.print_effect(f'\nSalud recuperada en {hp_txt}.')
            return True
        else:
            utilities.print_effect('\nNo se puede usar la poción. Vida del jugador al máximo.')
            return False
