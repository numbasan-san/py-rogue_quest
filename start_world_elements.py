
from player import *
from items.consumables import *
from items.equipment import *
from npc.enemies import *

class start_characters:

    def return_player(x, y):
        # hp, damage, defense, sprite, x, y
        return player(100, 25, 10, '@', x, y)
    
    def return_enemy():
        return [
            kelpie.kelpie.start_kelpie(),
            banshee.banshee.start_banshee(),
            ghoul.ghoul.start_ghoul(),
        ]

class start_items:

    def return_items():
        return [
            potion.potion(),
            potion_power.potion_power.start_potion_power(),
            sword.sword.start_sword(),
        ]
