
from player import *

from items.consumables.Potion import *
from items.consumables.Potion_Power import *
from items.equipment.Sword import *
from items.equipment.Shield import *
from items.equipment.Fire_Sword import *

from npc.enemies.kelpie import *
from npc.enemies.banshee import *
from npc.enemies.ghoul import *
from npc.enemies.titan import * 

class start_player:

    def __init__(self):
        self.player = player

    def return_player(self, x, y):
        # hp, damage, defense, sprite, x, y
        return self.player(10, 100, 0, '@', x, y)
    
class start_enemies:

    def __init__(self):
        self.kelpie = kelpie()
        self.banshee = banshee()
        self.ghoul = ghoul()
        self.titan = titan()

    def return_enemies(self):
        return [
            self.kelpie,
            self.banshee,
            self.ghoul,
            self.titan,
        ]

class start_items:

    def __init__(self):
        self.potion = potion()
        self.potion_power = potion_power()
        self.sword = sword()
        self.fire_sword = fire_sword()
        self.shield = shield()

    def return_items(self):
        return [
            self.potion,
            self.potion_power,
            self.sword,
            self.fire_sword,
            self.shield
        ]
