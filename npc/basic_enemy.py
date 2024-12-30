
import json
from colorama import *
from common_utilities import color_mappings
from npc.enemy_move_ia import move

info = json.load((open(f'npc/enemies/info/enemies_info.json', 'r', encoding='utf-8')))

class BasicEnemy:

    def __init__(self, name, hp, damage, defense, x, y, exp, range, taxonomy, alter_status=None, move_ia=None, strategy_ia=None):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.defense = defense
        self.sprite = name[0]
        self.descrip = info[(self.name).lower()]
        self.x = x
        self.y = y
        self.exp = exp
        self.range = range
        self.color = color_mappings.enemy_color_mapping.get(taxonomy, Fore.WHITE)
        self.taxonomy = color_mappings.enemy_taxonomy_mapping.get(taxonomy)
        self.alter_status = alter_status
        self.move_ia = move if move_ia is None else move_ia
        self.strategy_ia = strategy_ia
