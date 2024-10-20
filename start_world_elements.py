
from player import *

from items.consumables import *
from items.equipment import *
from items.environment import *
from colorama import *

from npc.enemies import *

class start_player:

    def __init__(self):
        # hp, damage, defense, sprite, x, y, color
        self.player = player(31, 100, 0, '@', Fore.LIGHTRED_EX)
    
    def get_player(self):
        return self.player

    def mod_player_coords(self, x, y):
        self.player.x = x
        self.player.y = y
        return self.player
    
class start_enemies:

    def return_enemies(self):
        return [
            kelpie.kelpie,
            banshee.banshee,
            ghoul.ghoul,
            titan.titan,
        ]

class start_items:

    def return_items(self):
        return [
            potion.potion,
            potion_power.potion_power,
            sword.sword,
            fire_sword.fire_sword,
            shield.shield,
            shield_medusa.shield_medusa,
        ]

    def return_stairs(self):
        return [
            stairs.stairs,
        ]
