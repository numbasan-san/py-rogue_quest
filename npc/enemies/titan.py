
from npc.basic_enemy import BasicEnemy as Enemy
from npc.enemy_move_ia import move as movement_ia
import config.setting as setting

class Titan(Enemy):

    def __init__(self, x=1, y=1):
        # name, hp, damage, defense, x, y, exp, range, taxonomy/color
        desc = (setting.get_language())["enemies"]["titan"]["description"]
        super().__init__('Titan', 100, 70, 10, x, y, 1000, 10, 3, "tt-T", desc=desc)
