
from player import *

from items.consumables import *
from items.equipment import *
from items.environment import *

from npc.enemies import *

class start_player:

    def __init__(self):
        # hp, damage, defense, sprite, x, y
        self.player = player(100, 100, 0, '@')

    def mod_player_coords(self, x, y):
        self.player.x = x
        self.player.y = y
        return self.player
    
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
