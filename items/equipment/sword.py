
from items.basic_equip import basic_equip
from common_utilities.utilities import *

class sword(basic_equip):

    def __init__(self, x=1, y=1):
        name = 'Espada'
        sprite = '/'
        damage = 10
        critic = 5
        defense = 0
        to_player = True
        # name, sprite, x, y, damage, critic, defense, rarity, func, to_player, battle_effect, desc, nonfunc
        super().__init__(name, sprite, x, y, damage, critic, defense, 1, func=self.use_function, to_player=to_player, desc='Es una espada normal', nonfunc=self.nonuse_function)

    def use_function(self, player):
        if player.equipment['sword'] is None or player.equipment['sword'].name != self.name:
            player.equipment['sword'] = self
            utilities.print_effect(f'\n[{self.name}] equipado.')
            player.damage += self.damage
        else:
            utilities.print_effect(f'[{self.name}] ya equipado.')

    def nonuse_function(self, player, msg):
        utilities.print_effect(msg)
        player.damage -= player.equipment['sword'].damage
        player.equipment['sword'] = None
