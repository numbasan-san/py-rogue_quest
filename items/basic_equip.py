
from items.basic_item import basic_item

class basic_equip(basic_item):

    def __init__(self, name, sprite, x, y, damage, critic, defense, rarity, func = None, to_player = True, battle_effect = None, desc = '', nonfunc = None):
        super().__init__(name, sprite, x, y, rarity, func = func, desc = desc, to_player = to_player)
        self.damage = damage
        self.critic = critic
        self.defense = defense
        self.battle_effect = battle_effect
        self.nonfunc = nonfunc
