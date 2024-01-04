
from player import *
from items import *
from enemies import *

class start_characters:

    def return_player(x, y):
        # hp, damage, defense, sprite, x, y
        return player(100, 5, 10, '@', x, y)
    
    def return_enemy():
        return [
            standar_enemy.standar_enemy.start_standar_enemy(),
        ]

class start_items:

    def return_items():
        return [
            potion.potion.start_potion(),
            potion_power.potion_power.start_potion_power(),
            sword.sword.start_sword(),
        ]
