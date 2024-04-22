
from items.consumables import *
from items.equipment import *
from items.environment import *

from npc.enemies import *

def return_object(name):
    object = {
        "pt-+": Potion.potion,
        "pp-x": Potion_Power.potion_power,
        "sw-/": Sword.sword,
        "fs-|": Fire_Sword.fire_sword,
        "sh-)": Shield.shield,
        "sm-]": Shield_Medusa.shield_medusa,
        "st-¬": Stairs.stairs,
        "kp-k": Kelpie.kelpie,
        "bs-b": Banshee.banshee,
        "gh-g": Ghoul.ghoul,
        "tt-t": Titan.titan,
    }
    return object[name]
