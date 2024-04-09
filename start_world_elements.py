
from player import *

from items.consumables import *
from items.equipment import *

from npc.enemies import *

class start_player:

    def __init__(self):
        self.player = player

    def return_player(self, x, y):
        # hp, damage, defense, sprite, x, y
        return self.player(100, 100, 0, '@', x, y)
    
class start_enemies:

    def return_enemies(self):
        return [
            kelpie.kelpie(),
            banshee.banshee(),
            ghoul.ghoul(),
            titan.titan(),
        ]

class start_items:

    def return_items(self):
        return [
            Potion.potion(),
            Potion_Power.potion_power(),
            Sword.sword(),
            Fire_Sword.fire_sword(),
            Shield.shield(),
            Shield_Medusa.shield_medusa(),
        ]
