
from npc.basic_enemy import BasicEnemy as Enemy
import config.setting as setting

class Ghoul(Enemy):

    def __init__(self, x=1, y=1):
        # name, hp, damage, defense, x, y, exp, range, taxonomy/color
        desc = (setting.get_language())["enemies"]["ghoul"]["description"]
        super().__init__('Ghoul', 100, 5, 10, x, y, 15, 2, 2, "gh-G", desc=desc)
