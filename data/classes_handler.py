
from items.consumables import *
from items.equipment import *
from items.environment import *

from npc.enemies import *

def get_class(name):
    classes = {

        # items
        "pt-+": potion.Potion,
        "pp-x": potion_power.PotionPower,
        
        # equipment
        "sw-/": sword.Sword,
        "fs-|": fire_sword.FireSword,
        "sh-)": shield.Shield,
        "sm-]": shield_medusa.ShieldMedusa,
        
        # enviroment items
        "st-¬": stairs.Stairs,

        # enemies
        "an-A": aracne.Aracne,
        "bs-B": banshee.Banshee,
        "cb-C": cerberos.Cerberos,
        "dg-D": dragon.Dragon,
        "fn-F": fenrir.Fenrir,
        "gh-G": ghoul.Ghoul,
        "jp-J": jupia.Jupia,
        "kp-K": kelpie.Kelpie,
        "lg-L": lugaru.Lugaru,
        "mm-M": mokele_mbembe.Mokele_mbembe,
        "nf-N": nefelin.Nefelin,
        "tt-T": titan.Titan,
        "yn-Y": yinn.Yinn
    }
    return classes[name]
