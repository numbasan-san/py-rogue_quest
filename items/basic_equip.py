
from items.basic_item import basic_item

class basic_equip(basic_item):

    def __init__(self, name, sprite, x, y, damage, critic, defense):
        super().__init__(name, sprite, x, y)
        self.damage = damage
        self.critic = critic
        self.defense = defense
