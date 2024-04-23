
from player import *

from items.consumables import *
from items.equipment import *
from items.environment import *

from npc.enemies import *

class start_player:

    def return_player():
        # hp, damage, defense, sprite, x, y
        return player(100, 100, 0, '@')
    
class start_enemies:

    def return_enemies(self):
        return [
            Kelpie.kelpie(),
            Banshee.banshee(),
            Ghoul.ghoul(),
            Titan.titan(),
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

    def return_stairs(self):
        return [
            Stairs.stairs(),
        ]
