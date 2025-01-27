
from items.basic_item import BasicItem

class BasicEquip(BasicItem):

    def __init__(self, name, sprite, x, y, damage, critic, defense, rarity, code, func = None, to_player = True, battle_effect = None, desc = '', nonfunc = None):
        super().__init__(name, sprite, x, y, rarity, code, func = func, desc = desc, to_player = to_player)
        self.damage = damage
        self.critic = critic
        self.defense = defense
        self.battle_effect = battle_effect
        self.nonfunc = nonfunc
