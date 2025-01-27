
from npc.basic_enemy import BasicEnemy as Enemy
import config.setting as setting

class Yinn(Enemy):

    def __init__(self, x=1, y=1):
        # name, hp, damage, defense, x, y, exp, range, taxonomy/color
        desc = (setting.get_language())["enemies"]["yinn"]["description"]
        super().__init__('Yinn', 100, 5, 10, x, y, 15, 2, 3, "yn-Y", desc=desc)
