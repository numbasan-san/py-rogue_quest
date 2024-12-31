
from world.player import *
from npc.enemies import *
from items.consumables import *
from items.equipment import *
from items.environment import *

from colorama import *

class StartPlayer:

    def __init__(self):
        # hp, damage, defense, sprite, x, y, color
        self.player = Player(10, 100, 0, '@', Fore.LIGHTRED_EX)
    
    def get_player(self):
        return self.player

    def mod_player_coords(self, x, y):
        self.player.x = x
        self.player.y = y
        return self.player

class StartEnemies:

    def return_enemies(self):
        return [
            aracne.Aracne,
            banshee.Banshee,
            cerberos.Cerberos,
            dragon.Dragon,
            fenrir.Fenrir,
            ghoul.Ghoul,
            jupia.Jupia,
            kelpie.Kelpie,
            lugaru.Lugaru,
            mokele_mbembe.Mokele_mbembe,
            nefelin.Nefelin,
            titan.Titan,
            yinn.Yinn,
        ]

class StartItems:

    def return_items(self):
        return [
            potion.Potion,
            potion_power.PotionPower,
            sword.Sword,
            fire_sword.FireSword,
            shield.Shield,
            shield_medusa.ShieldMedusa,
        ]

    def return_stairs(self):
        return [
            stairs.Stairs,
        ]
