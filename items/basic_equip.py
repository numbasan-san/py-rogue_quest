
from items.basic_item import basic_item

class basic_equip(basic_item):

    def __init__(self, code, name, sprite, x, y, damage, critic, defense, func = None, to_player = True, battle_effect = None, desc = '', nonfunc = None):
        super().__init__(code, name, sprite, x, y, func = func, to_player = to_player)
        self.damage = damage
        self.critic = critic
        self.defense = defense
        self.battle_effect = battle_effect
        self.desc = desc
        self.nonfunc = nonfunc
