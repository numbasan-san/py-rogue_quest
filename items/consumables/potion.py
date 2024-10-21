
from items.basic_item import basic_item
from common_utilities.utilities import *

class potion(basic_item):

    def __init__(self, x=1, y=1):
        name = 'Poción'
        sprite = '+'
        to_player = True
        desc = "Recupera 10 puntos de salud como máximo"
        # name, sprite, x, y, rarity, func, desc, to_player
        super().__init__(name, sprite, x, y, 2, func=self.use_function, desc=desc, to_player=to_player)

    def use_function(self, player):
        if player.hp < player.max_hp:
            hp_txt = '10' if (player.hp + 10) < player.max_hp else (player.max_hp - player.hp)
            player.hp = (player.hp + 10) if (player.hp + 10) < player.max_hp else player.max_hp
            utilities.print_effect(f'\nSalud recuperada en [{hp_txt}].')
            return True
        else:
            utilities.print_effect('\nTe detienes un segundo y piensas: "Mejor no lo desperdicio. No tengo heridas ahora".')
            return False
