
from colorama import *
from common_utilities import color_mappings
from npc.enemy_move_ia import move

class BasicEnemy:

    def __init__(self, name, hp, damage, defense, sprite, x, y, exp, range, color, alter_status=None, move_ia=None, strategy_ia=None):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defense = defense
        self.sprite = sprite
        self.x = x
        self.y = y
        self.exp = exp
        self.range = range
        self.color = color_mappings.enemy_color_mapping.get(color, Fore.WHITE)
        self.state = True
        self.alter_status = alter_status
        self.move_ia = move if move_ia is None else move_ia
        self.strategy_ia = strategy_ia
        self.buff_efects = []
