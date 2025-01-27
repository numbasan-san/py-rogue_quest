
from npc.basic_enemy import BasicEnemy as Enemy
import config.setting as setting

class Lugaru(Enemy):

    def __init__(self, x=1, y=1):
        # name, hp, damage, defense, x, y, exp, range, taxonomy/color
        desc = (setting.get_language())["enemies"]["lugaru"]["description"]
        super().__init__('Lugaru', 100, 5, 10, x, y, 15, 2, 1, "lg-L", desc=desc)
