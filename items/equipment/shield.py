
from items.basic_equip import basic_equip
from utilities import *

class shield(basic_equip):

    def __init__(self, x=1, y=1):
        name = 'Escudo'
        sprite = ')'
        damage = 0
        critic = 0
        defense = 10
        to_player = True
        super().__init__(name, sprite, x, y, damage, critic, defense, func=self.use_function, to_player=to_player, desc='Es un escudo normal', nonfunc=self.nonuse_function)

    def use_function(self, player):
        if player.equipment['shield'] is None or player.equipment['shield'].name != self.name:
            player.equipment['shield'] = self
            utilities.print_effect(f'\n[{self.name}] equipado.')
            player.defense = self.defense + player.base_defense
        else:
            utilities.print_effect(f'[{self.name}] ya equipado.')

    def nonuse_function(self, player, msg):
        utilities.print_effect(msg)
        player.defense -= player.equipment['shield'].defense
        player.equipment['shield'] = None
